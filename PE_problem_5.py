__author__ = 'zog'


"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import time
from project_euler_libs import *

div = []
for x in range(1,11,1):
    if (is_prime(x)):
        div.append(x)
    elif (x == 20):
        div.append(x)

print div

inc = 20
x = 20
idx = 0

while (1):
    x = x + inc
    rt = is_even_div(x,div,0)
    #print "x:",x,"rt:",rt
    #time.sleep(.2)
    if (rt == 1):
        #print "maybe x:",x
        tot_div = []
        for q in range(1,inc+1,1):
            tot_div.append(q)
        #print tot_div
        new_rt = is_even_div(x,tot_div,0)
        if (new_rt == 1):
            print "largest:",x
            break
    idx = idx + 1
    #if (idx % 10000000 == 0):
    #    print "idx:",idx
    #    print "x:",x,"rt:",rt

