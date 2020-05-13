import sqlite3
import json
conn = sqlite3.connect('../dashboard-app/sensors.db')
cursor = conn.cursor()

# for row in c.execute('SELECT * FROM telemetry ORDER BY timestamp DESC LIMIT 1'):
#         print (row)



cursor.execute('SELECT timestamp, temp FROM telemetry ORDER BY timestamp DESC LIMIT 1')

data = cursor.fetchall()



# print(result)

# data = {}
# data['timestamp'] = result[0]
# data['temp'] = result[1]

print (json.dumps(data))