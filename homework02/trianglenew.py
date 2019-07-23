import re

f = open("numbers.txt", "r+")

num = (f.read())
pattern = r"(\d?\d),"
results = re.findall(pattern, num)
mainresult = list(map(int, results))
print(mainresult)

for i in range(1000):
    if mainresult[0] + mainresult[1] > mainresult[2] and mainresult[0] + mainresult[2] > mainresult[1] and mainresult[
        1] + mainresult[2] > mainresult[0]:
        print("its triangle")
    else:
        print("its not triagnle")
    if mainresult[0] == mainresult[1] and mainresult[1] == mainresult[2] and mainresult[0] == mainresult[2]:
        print("its Equilateral")
    else:
        print("its not Equilateral")
    if mainresult[0] == mainresult[1] or mainresult[1] == mainresult[2] or mainresult[0] == mainresult[2]:
        print("its Isosceles")
    else:
        print("its not Isosceles")
    highest = int(max(mainresult))

    if mainresult[0] ** 2 + mainresult[1] ** 2 == highest ** 2:
        print("its right")
    else:
        print("its not right")
    mainresult.remove(mainresult[0])
    mainresult.remove(mainresult[0])
    mainresult.remove(mainresult[0])
