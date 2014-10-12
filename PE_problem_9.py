__author__ = 'zog'

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import math
from project_euler_libs import *

max_int =1000

for a in range(1,max_int,1):
    for b in range(1,max_int,1):
        c = math.sqrt(a**2 + b**2)
        total = a + b + c
        #print "a:",a,"b:",b,"c:",c,"total:", total
        if (total == 1000):
            print "a:",a,"b:",b,"c:",c
            product = a * b * c
            print "product:", product
            exit()

