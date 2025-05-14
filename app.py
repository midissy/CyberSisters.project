from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL config
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1201",
    database="cybersisters"
)

@app.route('/')
def index():
    return render_template("events.html")

@app.route('/events')
def show_events():
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT id, title, start_date, event_type FROM event")
    results = cur.fetchall()
    return jsonify(results)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM event WHERE id = %s", (event_id,))
    event = cur.fetchone()
    if event:
        return render_template("event_detail.html", event=event)
    return "Event not found", 404

if __name__ == '__main__':
    app.run(debug=True)


