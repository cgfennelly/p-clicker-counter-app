from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime, timedelta
from env import environment

app = Flask(__name__)

def init_db():
    with sqlite3.connect('app.db') as conn:
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS first_points (
                     id INTEGER PRIMARY KEY,
                     dttm TIMESTAMP
                     )
                     '''
                     )
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS second_points (
                     id INTEGER PRIMARY KEY,
                     dttm TIMESTAMP
                     )
                     '''
                     )
        conn.execute('''
                     CREATE TABLE IF NOT EXISTS third_points (
                     id INTEGER PRIMARY KEY,
                     dttm TIMESTAMP
                     )
                     '''
                     )

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#1st clicker
@app.route('/first-point', methods=['POST'])
def add_work_point():
    current_timestamp = datetime.now()

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO first_points (dttm) VALUES (?)",
        (current_timestamp,)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'message': 'point added'})

@app.route('/daily-first-points', methods=['GET'])
def get_daily_points():
    current_timestamp = datetime.now()
    today = current_timestamp.date()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM first_points WHERE DATE(dttm) = (?)", (today,))
    daily_first_points = cursor.fetchone()[0]
    conn.close()
    # Return the daily count as a JSON response
    return jsonify({'daily_first_points': daily_first_points})

@app.route('/total-first-points', methods=['GET'])
def get_daily_work_points():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM first_points")
    max_id = cursor.fetchone()[0]
    conn.close()
    # Return the maximum ID as a JSON response
    return jsonify({'max_id': max_id})

@app.route('/seven-day-avg-points', methods=['GET'])
def get_seven_day_avg_points():
    current_timestamp = datetime.now()
    today = current_timestamp.date()
    minus_seven_days = today - timedelta(days=7)
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("WITH daily_points AS (SELECT DATE(dttm) AS date, COUNT(*) AS total_points FROM first_points WHERE DATE(dttm) >= (?) AND DATE(dttm) < (?) GROUP BY DATE(dttm)) SELECT SUM(total_points) AS top_5_days_sum FROM (SELECT total_points FROM daily_points ORDER BY total_points DESC LIMIT 5)", (minus_seven_days, today,))
    return_value = cursor.fetchone()[0]
    if return_value is None:
        return_value = 0
    seven_day_avg_points = round(return_value/5,0)
    conn.close()
    # Return the daily count as a JSON response
    return jsonify({'seven_day_avg_points': seven_day_avg_points})

# 2nd clicker
@app.route('/second-point', methods=['POST'])
def add_second_point():
    current_timestamp = datetime.now()

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO second_points (dttm) VALUES (?)",
        (current_timestamp,)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'message': 'point added'})

@app.route('/daily-second-points', methods=['GET'])
def get_daily_second_points():
    current_timestamp = datetime.now()
    today = current_timestamp.date()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM second_points WHERE DATE(dttm) = (?)", (today,))
    daily_second_points = cursor.fetchone()[0]
    conn.close()
    # Return the daily count as a JSON response
    return jsonify({'daily_second_points': daily_second_points})

@app.route('/total-second-points', methods=['GET'])
def get_total_second_points():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM second_points")
    max_points = cursor.fetchone()[0]
    conn.close()
    # Return the maximum ID as a JSON response
    return jsonify({'total_second_points': max_points})

# 3rd clicker
@app.route('/third-point', methods=['POST'])
def add_third_point():
    current_timestamp = datetime.now()

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO third_points (dttm) VALUES (?)",
        (current_timestamp,)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'message': 'point added'})

@app.route('/daily-third-points', methods=['GET'])
def get_daily_third_points():
    current_timestamp = datetime.now()
    today = current_timestamp.date()
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM third_points WHERE DATE(dttm) = (?)", (today,))
    daily_third_points = cursor.fetchone()[0]
    conn.close()
    # Return the daily count as a JSON response
    return jsonify({'daily_third_points': daily_third_points})

@app.route('/total-third-points', methods=['GET'])
def get_total_third_points():
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM third_points")
    max_points = cursor.fetchone()[0]
    conn.close()
    # Return the maximum ID as a JSON response
    return jsonify({'total_third_points': max_points})



if __name__ == '__main__':
    init_db()
    env = environment()
    if env == "local":
        app.run(debug=True) # local run
    elif env == "prod":  
        app.run(host='0.0.0.0', port=8077, debug=True)
    else:
        print("environment not configured")

# Statement to test this:
# curl -X POST -H "Content-Type: application/json"  http://127.0.0.1:5000/first-point
# curl -X POST -H "Content-Type: application/json" http://193.123.185.59:8077/first-point

