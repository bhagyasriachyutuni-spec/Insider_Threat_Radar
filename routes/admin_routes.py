from flask import Blueprint, render_template, redirect, session
from utils.db import get_db_connection

admin_bp = Blueprint('admin', __name__)

# ---------------- DASHBOARD ----------------
from flask import Blueprint, render_template, redirect, session
from utils.db import get_db_connection

admin_bp = Blueprint('admin', __name__)

# ---------------- DASHBOARD ----------------
@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect('/login_admin')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # USERS
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # ALERTS
    cursor.execute("""
        SELECT * FROM admin_alerts
        ORDER BY created_at DESC
        LIMIT 10
    """)
    notifications = cursor.fetchall()

    # 🔔 UNREAD ALERT COUNT
    cursor.execute("""
        SELECT COUNT(*) AS unread_count
        FROM admin_alerts
        WHERE status='unread'
    """)
    unread = cursor.fetchone()['unread_count']

    conn.close()

    return render_template(
        'admin/dashboard.html',
        users=users,
        notifications=notifications,
        unread_count=unread
    )


# ---------------- USER MANAGEMENT ----------------
@admin_bp.route('/admin/toggle/<user_id>')
def toggle_user(user_id):
    if 'admin_id' not in session:
        return redirect('/login_admin')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT status FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return redirect('/admin/dashboard')

    new_status = 'archived' if user['status'] == 'active' else 'active'

    cursor.execute(
        "UPDATE users SET status=%s WHERE id=%s",
        (new_status, user_id)
    )

    conn.commit()
    conn.close()

    return redirect('/admin/dashboard')


# ---------------- ADMIN ALERTS PAGE ----------------
@admin_bp.route('/admin/activities')
def admin_activities():
    if 'admin_id' not in session:
        return redirect('/login_admin')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM admin_alerts
        ORDER BY created_at DESC
    """)
    alerts = cursor.fetchall()

    conn.close()

    return render_template('admin/activities.html', alerts=alerts)


# ---------------- MARK ALERT AS READ ----------------
@admin_bp.route('/admin/mark_read/<int:id>')
def mark_read(id):
    if 'admin_id' not in session:
        return redirect('/login_admin')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE admin_alerts SET status='read' WHERE id=%s",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/admin/dashboard')