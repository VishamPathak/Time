## Time
A class that handles time-related tasks

### Formula
`import time`
1. time.time()
- Returns floating-point numbers in seconds passed since epoch (January 1st, 1970, 00:00 at UTC)
- Use it for Date arithmetics (etc. duration)
```python
import time
#Function: time()
print("Second since epoch = " + str(time.time()))
```

2. time.sleep()
- Suspend (delays) execution for a given number of seconds `time.sleep(3.3)` Pause our code for 3.3 seconds