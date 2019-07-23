# numbers = [input("enter 3 numbers please")]
'''
inputs = []
x=3
for i in range(3):  # loop 3 times
	inputs.append(input("enter number"))
print(inputs)
'''
print('enter 3 numbers with space')
numbers = list(map(int, input().split()))
print(numbers)
if numbers[0] + numbers[1] > numbers[2] and numbers[1] + numbers[2] > numbers[0] and numbers[2] + numbers[0] > numbers[
    1]:
    print("its triangle")
else:
    print("its not triagnle")
if numbers[0] == numbers[1] and numbers[1] == numbers[2] and numbers[0] == numbers[2]:
    print("its Equilateral")
else:
    print("its not Equilateral")
if numbers[0] == numbers[1] or numbers[1] == numbers[2] or numbers[0] == numbers[2]:
    print("its Isosceles")
else:
    print("its not Isosceles")
highest = int(max(numbers))
#numbers.remove(highest)
if numbers[0] ** 2 + numbers[1] ** 2 == highest ** 2:
    print("its right")
else:
    print("its not right")
