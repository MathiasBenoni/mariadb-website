import mariadb
import sys

from more_itertools import flatten

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

    adjective_list_with_values = [item for row in results for item in row]

    print(adjective_list_with_values)
    
    cur.close()
    conn.close()
    return adjective_list_with_values

def write(x):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT adjective FROM adjectives;')
    adjectives_already_in_database = [row[0] for row in cur.fetchall()]

    if x in adjectives_already_in_database:
        cur.execute('UPDATE adjectives SET counter = counter + 1 WHERE adjective = ?;', (x,))
    else:

        cur.execute('INSERT INTO adjectives (adjective, counter) VALUES (?, 1);', (x,))

    conn.commit()
    cur.close()
    conn.close()