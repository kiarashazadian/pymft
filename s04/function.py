# multiply (m,n)

def multiply(m, n):
    res = m * n
    return res


def sum_of_numbers(n):
    return n * (n + 1) / 2


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


print(sum_of_numbers(100))
print(is_prime(9))
print(multiply(2, 5))

def my_sum(*args):
    return sum(args)

print(my_sum(1,2,3,4,5,6))