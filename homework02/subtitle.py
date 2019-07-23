import re
f = open('file.txt', encoding='utf-8')
text = f.read()
pattern = r"(\d\d):(\d\d):(\d\d,\d\d\d)"
results = re.findall(pattern, text)
#secounds = list(map(int, results))
print(results)
mylist=[]
for i in range(10):
    for k in range(2):
        mylist=results[i][k]

print(mylist)
'''
print(secounds)
pattern2=r"(\d\d):"
results2 = re.findall(pattern2, text)
minutes = list(map(int, results2))
print(minutes)
pattern3 = r"(\d\d):"
results3 = re.findall(pattern3, text)
houres = list(map(int, results3))
print(houres)
'''
