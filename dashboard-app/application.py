from flask import Flask, escape, request, render_template, jsonify
import sqlite3
import json

app = Flask(__name__)

@app.route('/data')
def data():
    conn = sqlite3.connect('sensors.db')
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp, temp FROM telemetry ORDER BY timestamp DESC LIMIT 1')
    data = cursor.fetchall()[0]
    return jsonify(data)

@app.route('/')
def hello():
    return render_template('main.html')