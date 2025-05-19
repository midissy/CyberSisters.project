from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb, mysql.connector

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1201'
app.config['MYSQL_DB'] = 'cybersisters'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        deadline = request.form['deadline']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO event (title, content, deadline) VALUES (%s, %s, %s)", (title, content, deadline))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/calendar')
def calendar():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM events ORDER BY ID")
    event = cur.fetchall()
    return render_template('calendar.html', event=event)


if __name__ == "__main__":
    app.run(debug=True)
