import mariadb
import sys


try:
    conn = mariadb.connect(
        user="pythonuser",
        password="pythonpass",
        host="127.0.0.1",
        port=3306,
        database="adjectives"
    )   
    
    print('Success!')

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit (1)

# Vi trenger CURSOR for å utføre QUERIES
cur = conn.cursor()

cur.execute('SELECT adjective FROM adjectives;')


for row in cur:
    text = ''
    for value in row:
        text += str(value) + '\t\t'

    print(text)

cur.close()



def write(x):
    cur = conn.cursor()
    cur.execute(f'INSERT INTO adjectives (adjective) VALUES ("{x}");')

    cur.close()
