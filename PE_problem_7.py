__author__ = 'zog'


"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

from project_euler_libs import *
import time

prime_list = gen_prime_list(10001)

answer = prime_list[-1]
len_prime = len(prime_list)
print "answer:",answer, "prime_len:",len_prime



