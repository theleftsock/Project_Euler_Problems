__author__ = 'zog'
print "hello world"

total = 0
for x in range(1,1000,1):
    if (x % 3 == 0) or (x % 5 == 0):
        total += x
        print "x: ", x, "total: ", total


print total