__author__ = 'zog'

from project_euler_libs import *
import networkx as nx
import matplotlib.pyplot as plt
import math as m

big_num = 2**1000
print "big_num: ",big_num

total = 0
for x in str(big_num):
    print "x: ",x
    total = total + int(x)

print "total: ", total