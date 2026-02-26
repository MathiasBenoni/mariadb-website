import mariadb
import sys

def get_connection():
    try:
        conn = mariadb.connect(
            user="pythonuser",
            password="pythonpass",
            host="127.0.0.1",
            port=3306,
            database="adjectives"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

def get_adjectives():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT adjective, counter FROM adjectives;')
    results = cur.fetchall()
    cur.close()
    conn.close()

    # {"happy": 5, "pink": 3, "no": 2}
    return {adjective: counter for adjective, counter in results}

def write(x):
    conn = get_connection()
    cur = conn.cursor()

    # Use INSERT ... ON DUPLICATE KEY UPDATE to avoid a separate SELECT
    cur.execute('''
        INSERT INTO adjectives (adjective, counter) VALUES (?, 1)
        ON DUPLICATE KEY UPDATE counter = counter + 1;
    ''', (x,))

    conn.commit()
    cur.close()
    conn.close()