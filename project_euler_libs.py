__author__ = 'zog'

import math
#function takes an array of finbonaccit numbers and computes the next fibonaccit number
def get_next_fib(fib_ar):
    next_fib = 0
    next_fib = fib_ar[-1]
    next_fib = next_fib + fib_ar[-2]
    return next_fib

#brute force solution for prime factors
#
def prime_factors(n): #generate a list of prime factor
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

def gen_prime_list(n): #generate a list of prime number of length n
    i = 1
    prime_list = [2]
    while(len(prime_list) < n):
        i += 2
        if (is_prime(i) == True):
            prime_list.append(i)
    return prime_list


def gen_next_prime(n): #generate the next prime greater than the number sent
    i = n + 1
    if (i % 2 == 0):
        i = i + 1
    while (is_prime(i) == False):
        i += 2
    return i

def is_prime(n): #return true if the number sent is prime
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

def is_even_div(num,div,opt): #takes a number, a list of divisors, and returns 1 if divisible
    for x in div:
        if (num % x != 0):
            if (opt == 1):
                print "not divisible by",x,"remainder",num % x
            return 0
    return 1

def get_list_product(list):
    product = 1
    for x in list:
        x = int(x)
        product = product * x
    return product

def max_sub_list(list,item_count):
    adj_items = []
    max_product = 0
    max_adj_items = []
    for item in list:
        print "item:",item
        if (item == '\n'):
            continue
        if (len(adj_items) < item_count):
            adj_digits.append(item)
            continue
        adj_items.pop(0)
        adj_items.append(item)
        product = get_list_product(adj_items)
        print "product:",product
        if (product > max_product) and (len(adj_items) == item_count):
            max_product = product
            max_adj_items = adj_items[:]
    return max_product