import serial
import json
import schedule
import time

ser = serial.Serial('/dev/cu.usbmodem141101')



# while True:
#     value = ser.readline().decode().strip()
#     value = json.loads(value)


#     print (value["rpm"])

def job():
    # print("I'm working...")
    value = ser.readline().decode().strip()
    # value = json.loads(value)
    # print (value["rpm"])
    print(value)

schedule.every(.1).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(.1)