__author__ = 'zog'
print "hello world"

import math
#function takes an array of finbonaccit numbers and computes the next fibonaccit number
def get_next_fib(fib_ar):
    next_fib = 0
    next_fib = fib_ar[-1]
    next_fib = next_fib + fib_ar[-2]
    return next_fib

#brute force solution for prime factors
#
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#takes a number and returns 1 if that number is a palindrome
def num_is_palindrome(num):
    if (str(num) == str(num)[::-1]):
        return 1
    else:
        return 0

def is_even_div(num,div,opt):
    for x in div:
        if (num % x != 0):
            if (opt == 1):
                print "not divisible by",x,"remainder",num % x
            return 0
    return 1
