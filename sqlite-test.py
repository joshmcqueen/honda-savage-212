import sqlite3
import os
import threading
import random
import time
import datetime

# get DB up and running
database = "example.db"

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
    time.sleep(1)


genTemp()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# conn.close()
