__author__ = 'zog'

from project_euler_libs import *

#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural
## numbers and the square of the sum is 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one
## hundred natural numbers and the square of the sum.

sum_of_sq = 0
sum = 0
for x in range (1,101,1):
    sum_of_sq = sum_of_sq + x**2
    sum += x

answer = sum**2 - sum_of_sq
print "answer:",answer


