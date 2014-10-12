__author__ = 'zog'


from project_euler_libs import *

factor1 = 1000
factor2 = 1000
palindromes = []

for x in xrange(factor1,100,-1):
    for y in range(factor2,100,-1):
        num = x * y
        #print "x:",x,"y:",y,"num:",num
        if (num_is_palindrome(num)):
            palindromes.append(num)

max_p = max(palindromes)
print "max palindrome:",max_p