import threading
import random

def genTemp():
  threading.Timer(0.5, genTemp).start()
  print(random.randint(50,60))

def genRPM():
  threading.Timer(0.05, genRPM).start()
  print(random.randint(1000,2000))

def genSpeed():
  threading.Timer(0.1, genSpeed).start()
  print(random.randint(1,20))

genTemp()
genRPM()
genSpeed()