import random
upper = 1024

secret = random.randint(1, upper)
print(secret)

while True:
    mynum = int(input("type a number"))
    if mynum > secret:
        print("bigger")
    elif mynum < secret:
        print("smaller")
    else:
        print("congrajolations")
        break