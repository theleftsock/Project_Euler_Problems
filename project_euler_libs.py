__author__ = 'zog'
print "hello world"

def get_next_fib(fib_ar):
    next_fib = 0
    next_fib = fib_ar[-1]
    next_fib = next_fib + fib_ar[-2]
    return next_fib