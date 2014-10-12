__author__ = 'zog'

from project_euler_libs import *

n = 13195
n = 600851475143
factors = prime_factors(n)
print factors

max_factor = max(factors)
print "max_prime_factor:",max_factor