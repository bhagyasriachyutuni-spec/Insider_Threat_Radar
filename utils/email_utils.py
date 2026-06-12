from utils.db import get_db_connection


def notify_admin(message):
    print("ADMIN ALERT:", message)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO admin_alerts (message, status)
            VALUES (%s, %s)
        """, (message, 'unread'))

        conn.commit()
        conn.close()

        print("✅ Alert saved to DB")

    except Exception as e:
        print("DB Alert Error:", e)


def notify_manager(message):
    print("MANAGER ALERT:", message)