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
    cur.execute('SELECT adjective FROM adjectives;')
    gotten_adjectives = []

    for row in cur:
        text = ''
        for value in row:
            text += str(value)
            gotten_adjectives.append(text)
        print(text)
    
    cur.close()
    conn.close()
    return gotten_adjectives

def write(x):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO adjectives (adjective) VALUES (?);', (x,))
    conn.commit()
    cur.close()
    conn.close()