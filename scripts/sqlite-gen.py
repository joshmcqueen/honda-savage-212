import sqlite3
import os
import threading
import random
import time
import datetime

print("Running...")
# get DB up and running
database = "../dashboard-app/sensors.db"

if os.path.exists(database):
  os.remove(database)

conn = sqlite3.connect(database)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE telemetry (timestamp TEXT, temp INTEGER)''')


while True:
    timestamp = datetime.datetime.utcnow().isoformat()
    temp = random.randint(1,20)
    c.execute("INSERT INTO telemetry (timestamp, temp) VALUES(?, ?)", (timestamp, temp)) 
    conn.commit()
    time.sleep(.1)

