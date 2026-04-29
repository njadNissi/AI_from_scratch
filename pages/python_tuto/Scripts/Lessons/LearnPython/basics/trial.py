class St:
    def __init__(m, a, b):
        m._a = a
        m.__b = b

    def setb(o, b):
        o.__b = b

    def getb(o):
        return o.__b


St.x = -1
s3 = St(0, 1)
s3.r = True
print(s3.x)

s4 = St(0, 1)
print(s4.x)
