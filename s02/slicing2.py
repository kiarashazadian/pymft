my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = my_list[:3]
lst2 = my_list[3:6]
lst3 = my_list[6:]
print(*lst3+lst2+lst)
