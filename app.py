import psycopg2

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 

def db_connect():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="root"
    )
    return conn

@app.route('/')
def index():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    conn = db_connect()
    cur = conn.cursor()
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cur.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    conn = db_connect()
    cur = conn.cursor()
    name = request.form['name']
    email = request.form['email']
    cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))
