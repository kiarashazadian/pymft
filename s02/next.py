mynumber = 11
result = not (10 <= mynumber <= 20 or 30 <= mynumber <= 40)
print(result)

result2 = 10 <= mynumber <= 40 and not (20 < mynumber < 30)
print(result2)