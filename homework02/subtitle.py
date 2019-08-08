import re

f = open('file.txt', encoding='utf-8')
text = f.read()
pattern = r"(\d\d):(\d\d):(\d\d),(\d\d\d) --> (\d\d):(\d\d):(\d\d),(\d\d\d)"
results = re.findall(pattern, text)
# secounds = list(map(int, results))
k = 0
j = 0
newresult = []
for i in results:
    newresult.append(list(results[k]))
    k += 1


print(newresult)
