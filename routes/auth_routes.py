from flask import Blueprint, render_template, request, redirect, session
from utils.db import get_db_connection
from utils.keystroke import save_pattern, check_pattern
from utils.email_utils import notify_admin, notify_manager

auth_bp = Blueprint('auth', __name__)

# ✅ ADMIN
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"


# ---------------- REGISTER ----------------
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        password = request.form['password']
        question = request.form['question']
        answer = request.form['answer']
        pattern = request.form.get('pattern')

        print("REGISTER PATTERN:", pattern)

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (id, email, password, role, security_question, security_answer)
            VALUES (%s,%s,%s,'user',%s,%s)
        """, (user_id, email, password, question, answer))

        conn.commit()
        conn.close()

        # ✅ SAVE PATTERN
        try:
            if pattern:
                save_pattern(user_id, pattern)
            else:
                print("❌ No pattern received during REGISTER")
        except Exception as e:
            print("Pattern Save Error:", e)

        return redirect('/login_user')

    return render_template('auth/register.html')


# ---------------- USER LOGIN ----------------
@auth_bp.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']
        pattern = request.form.get('pattern')

        print("LOGIN PATTERN:", pattern)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE id=%s AND password=%s AND role='user'",
            (user_id, password)
        )
        user = cursor.fetchone()

        if user:

            # 🚫 BLOCKED USER
            if user['status'] == 'archived':
                return render_template(
                    'auth/login_user.html',
                    error="🚫 Access blocked by Admin"
                )

            # ✅ KEYSTROKE CHECK (NO BLOCKING)
            try:
                if pattern:
                    is_match = check_pattern(user_id, pattern)
                    print("MATCH RESULT:", is_match)

                    if not is_match:
                        # 🚨 ONLY ALERT (NO BLOCK)
                        notify_admin(
                            f"⚠️ Behavior mismatch detected for user: {user_id}"
                        )

                        # Optional: store flag in session
                        session['anomaly'] = True
                else:
                    print("❌ No pattern received during LOGIN")

            except Exception as e:
                print("Pattern Check Error:", e)

            # ✅ ALWAYS LOGIN
            session['user_id'] = user['id']

            return redirect('/user/dashboard')

        return render_template(
            'auth/login_user.html',
            error="Invalid Credentials"
        )

    return render_template('auth/login_user.html')


# ---------------- ADMIN LOGIN ----------------
@auth_bp.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        user_id = request.form['id']
        password = request.form['password']

        if user_id == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_id'] = "admin"
            return redirect('/admin/dashboard')

        return render_template(
            'auth/login_admin.html',
            error="Invalid Admin Credentials"
        )

    return render_template('auth/login_admin.html')


# ---------------- SEND EMAIL ----------------
@auth_bp.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        to = request.form['to']
        subject = request.form['subject']
        message = request.form['message']
        user = session.get('user_id', 'unknown')

        # 🚨 DOMAIN CHECK
        if not to.endswith("@savantis.com"):
            notify_manager(
                f"⚠️ External Email Alert\nUser: {user}\nTo: {to}\nSubject: {subject}"
            )

        print(f"[EMAIL LOG] {user} -> {to} | {subject}")

        return render_template(
            'user/send_email.html',
            success="Email sent successfully!"
        )

    return render_template('user/send_email.html')


# ---------------- FORGOT PASSWORD ----------------
@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        user_id = request.form['id']
        email = request.form['email']
        answer = request.form['answer']
        new_password = request.form['new_password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE id=%s AND email=%s",
            (user_id, email)
        )
        user = cursor.fetchone()

        if user and user['security_answer'] == answer:
            cursor.execute(
                "UPDATE users SET password=%s WHERE id=%s",
                (new_password, user_id)
            )
            conn.commit()
            conn.close()

            return redirect('/login_user')

        return render_template(
            'auth/forgot_password.html',
            error="Invalid details"
        )

    return render_template('auth/forgot_password.html')


# ---------------- LOGOUT ----------------
@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')