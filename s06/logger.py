import time
def logger(fn):
    def inner(*args):
        res=fn(*args)
    return inner
open("logs.txt",mode="a")
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res=res*i
    return n
print(factorial(7))