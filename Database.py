import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'task_manager_db'
}

def get_db():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()
        yield db, cursor
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

def execute_query(db, cursor, query, params=None):
    cursor.execute(query, params)
    db.commit()
    return cursor

def fetch_one(cursor):
    return cursor.fetchone()

def fetch_all(cursor):
    return cursor.fetchall()
