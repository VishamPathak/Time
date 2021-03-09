import time
#Function: time()
print("Second since epoch = " + str(time.ctime()))

countdown = 3
while(countdown >= 0):
  print(countdown)
  countdown -= 1
  time.sleep(1)
print("VROOOOM!")

startTime = time.time()
userName = input("Type your name: ")
endTime = time.time()
print("Elapsed time: " + str(endTime-startTime))