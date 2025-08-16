import datetime as dt

startTime = dt.datetime.now()
i = 0
while i < 100000:
    print(i)
    i += 1

endTime = dt.datetime.now()
print(endTime - startTime)
