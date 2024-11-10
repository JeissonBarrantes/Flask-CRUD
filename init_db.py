import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="postgres",
    password="root"
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
)
""")

cur.execute("""INSERT INTO users(name, email, password) VALUES ('John', 'john@gmail.com', '123456')""")

conn.commit()
cur.close()
conn.close()