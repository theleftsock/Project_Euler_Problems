__author__ = 'zog'

from project_euler_libs import *
import networkx as nx
import matplotlib.pyplot as plt
import math as m
import re

f = open('PE_Problem_18_data.txt', 'r')
file_lines = []
file_lines = f.readlines()
print file_lines

first_line = []
second_line = []
new_line = []
counter = 0
rev_file_lines = []

for fl in reversed(file_lines):  # reversing the file and splitting the lines into lists
    rev_file_lines.append(fl.split())

while (len(rev_file_lines) > 1 and counter < 100):  # run while the len of our list is greater than 1
    first_line = rev_file_lines[0]
    second_line = rev_file_lines[1]
    index = 0
    new_line = []
    for snum in second_line:  # we start on the second line to combine it with the first
        print "snum: ", snum
        left_num = int(snum) + int(first_line[0+index])
        right_num = int(snum) + int(first_line[1+index])
        print "left_num: ", left_num
        print "right_num: ", right_num
        if (left_num > right_num):
            new_num = left_num
        else:
            new_num = right_num
        new_line.append(new_num)
        index += 1
        print "len of new_line: ", len(new_line), "new_line : ", new_line
    del rev_file_lines[0]
    del rev_file_lines[0]
    rev_file_lines.insert(0, new_line)
    counter += 1