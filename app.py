import MySQLdb
from flask import Flask, render_template, jsonify
import mysql.connector
#import MySQL, MySQLdb

app = Flask(__name__)

events = [
    {
        'todo' : 'Tutorial for Ann',
        'date' : '2025-05-05',
    },
    {
        'todo' : 'Mathematics exam',
        'date' : '2025-05-23',
    }
]

# MySQL config
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1201",
    database="cybersisters"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route ('/calendar')
def calendar():
    return render_template('calendar.html', events = events)

if __name__ == "__main__":
    app.run(debug=True)
