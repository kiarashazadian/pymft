mylist = [1, 2, [3, [4, 5], 6], 7]
output = []


def removeNestings(l):
    for i in l:
        if type(i) == list:
            removeNestings(i)
        else:
            output.append(i)


removeNestings(mylist)
print(output)
