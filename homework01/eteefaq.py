# 1 & 2
my_list = [50.3, 338.4, 626.5, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]
duration = []
my_list2 = []
n = 9
i = 0
x = 0
t1 = 300
t2 = 400
while i < n:
    duration.append(my_list[x + 1] - my_list[x])
    if duration[x] <= t1:
        int(duration[x])
        my_list2.append("s")
    elif duration[x] >= t2:
        my_list2.append("l")
    else:
        my_list2.append("m")
    x += 1
    i += 1
print(duration)
print(*my_list2)


