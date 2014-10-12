__author__ = 'zog'

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from project_euler_libs import *

next_prime = 2
total_primes = 0
upper_limit = 2*10**6
idx = 0
while (next_prime < upper_limit):
    total_primes = total_primes + next_prime
    next_prime = gen_next_prime(next_prime)
    #print "next_prime:",next_prime


print "total:", total_primes

