def power2(number):
    q = 2
    k = 1
    i = 1
    while i <= number:
        yield k
        k = q * q
        q += 1
        i += 1


p = power2(1_000_000)
prms = [i for i in p]

print(prms)
