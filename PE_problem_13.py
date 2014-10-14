__author__ = 'zog'

from project_euler_libs import *

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers in the data file

fn = 'PE_problem_13_data.txt'
fh = open(fn,'r')
file_data = fh.read()
file_lines = file_data.split('\n')

print "file_line:",file_lines

total = 0
for fl in file_lines:
    fl = int(fl)
    total = fl + total

mini_total = 0
idx = 1
tot_str = ''

for digit in str(total):
    print "digit:",digit,"idx:",idx
    tot_str = tot_str + digit
    if (idx >= 10):
        break
    idx = idx + 1

print "first_ten_digit:",tot_str