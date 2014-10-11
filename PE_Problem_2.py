__author__ = 'zog'

from project_euler_libs import *

fib_val = 0
total = 0
even_total = 2
fib_ar = [1,2]
fib_val = 0
while (fib_val < 4*10**6):
    fib_val = get_next_fib(fib_ar)
    print "fib_val:", fib_val
    fib_ar.append(fib_val)
    if (fib_val % 2 == 0):
        even_total = even_total + fib_val
        print "fib_val:",fib_val, "total: ", even_total

print even_total

