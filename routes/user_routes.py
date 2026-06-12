from flask import Blueprint, render_template, request, session, redirect
from utils.model_utils import predict_user
from utils.db import get_db_connection
from utils.email_utils import notify_admin   # ⭐ IMPORTANT

user_bp = Blueprint('user', __name__)

# ---------------- DASHBOARD ----------------
@user_bp.route('/user/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login_user')
    return render_template('user/dashboard.html')


# ---------------- PREDICTION PAGE ----------------
@user_bp.route('/user/prediction', methods=['GET', 'POST'])
def prediction():
    if 'user_id' not in session:
        return redirect('/login_user')

    if request.method == 'POST':
        user_id = session['user_id']

        try:
            data = {
                'total_emails': float(request.form['emails']),
                'total_attachments': float(request.form['attachments']),
                'avg_email_size': float(request.form['size']),
                'off_hour_emails': float(request.form['off_hours']),
                'weekend_emails': float(request.form['weekend']),
                'O': float(request.form['O']),
                'C': float(request.form['C']),
                'E': float(request.form['E']),
                'A': float(request.form['A']),
                'N': float(request.form['N'])
            }
        except:
            return "Invalid Input"

        label, score, level = predict_user(data)

        conn = get_db_connection()
        cursor = conn.cursor()

        # Save prediction
        cursor.execute("""
            INSERT INTO predictions (user_id, input_data, prediction, risk_score, risk_level)
            VALUES (%s,%s,%s,%s,%s)
        """, (user_id, str(data), label, score, level))

        # 🚨 ADMIN ALERT IF HIGH RISK
        if level == "High":
            notify_admin(
                f"🚨 Suspicious activity detected!\nUser: {user_id}\nRisk Score: {score}"
            )

        conn.commit()
        conn.close()

        return render_template(
            'user/prediction.html',
            result=label,
            score=score,
            level=level
        )

    return render_template('user/prediction.html')


# ---------------- HISTORY ----------------
@user_bp.route('/user/history')
def history():
    if 'user_id' not in session:
        return redirect('/login_user')

    user_id = session['user_id']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM predictions 
        WHERE user_id=%s 
        ORDER BY timestamp DESC
    """, (user_id,))

    data = cursor.fetchall()
    conn.close()

    return render_template('user/history.html', data=data)