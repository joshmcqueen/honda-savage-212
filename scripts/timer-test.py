import os
import sqlite3
import serial
import random
import json
import time
import datetime

print("Starting...")

# setup database
database = "../dashboard-app/sensors.db"

if os.path.exists(database):
  os.remove(database)

conn = sqlite3.connect(database)
cursor = conn.cursor()

# create table
cursor.execute('''CREATE TABLE telemetry (timestamp TEXT, temp INTEGER)''')

# open serial connection
ser = serial.Serial('/dev/cu.usbmodem141101')

# setup globals
_TEMP = 0

# setup timers
TIMER_LIMIT = .1
setTimer = time.time()

# function to write data
def writeToDatabase():
    timestamp = datetime.datetime.utcnow().isoformat()
    temp = random.randint(1,20)
    cursor.execute("INSERT INTO telemetry (timestamp, temp) VALUES(?, ?)", (timestamp, _TEMP))
    conn.commit()

# loop that runs non-stop
while(1):
    try:
        # read the values in
        value = ser.readline()
        value = value.decode().strip()
        value = json.loads(value)
        _TEMP = value["rpm"]
    except KeyboardInterrupt:
        sys.exit()
    except:
        # skip errors
        continue

    # logic to inturupt loop
    if(time.time() - setTimer >= TIMER_LIMIT):
            writeToDatabase()
            setTimer = time.time()
