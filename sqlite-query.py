import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 1'):
        print (row)