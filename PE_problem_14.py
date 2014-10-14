__author__ = 'zog'


#The following iterative sequence is defined for the set of positive integers
#n - n/2 (n is even)
#n - 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

from project_euler_libs import *

max_hops = 0
max_num = 0
num = 1
hops_dict = {}
while (num < 1000000):
    new_num = num
    hops = 0
    while (new_num != 1):
        if (new_num % 2 == 0):
            new_num = new_num/2
            #print "new_num_even:",new_num
        elif (new_num % 2 != 0):
            new_num = 3*new_num+1
        hops = hops + 1
        #print "new_num:",new_num,"hops:",hops
        #if new_num in hops_dict.keys():
            #hops = hops + hops_dict[new_num]
            #break
    #hops_dict[num] = hops
    #print hops_dict
    if (hops > max_hops):
        max_hops = hops
        max_num = num
    num = num + 1
    #print "num:",num
    if (num % 100000 == 0):
        print "num:", num, "max_hops:",max_hops

print "max_hops:",max_hops,"max_num:",max_num
