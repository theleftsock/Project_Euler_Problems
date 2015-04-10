__author__ = 'zog'

from project_euler_libs import *
import networkx as nx
import matplotlib.pyplot as plt
import math as m
import re

"""
  convert numbers to works
  http://www.tools4noobs.com/online_tools/number_spell_words/
"""

f = open("numbers_as_words.txt", 'r')
file_lines = f.readlines()

total = 0
for line in file_lines:
    line.rstrip('\n')
    vals = line.split()
    new_line = ""
    for val in vals:
        print "val:", val
        new_line = new_line+val
    print "line:", line, "line total:",len(line), "new_line:",new_line
    total = len(new_line) + total
    searchObj = re.search( r'-', line, re.M|re.I)
    if searchObj:
        total = total - 1
        print "dash_found_line:",line
    print "total: ", total
total = total + (9 * 99 * 3)
print "total: ", total