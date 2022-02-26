sample = [1, 12, 34, 3, 16, 99, 13]


def find_greatest(numlist):
    temp = numlist[0]
    for i in range(1, len(numlist)):
        if numlist[i] > temp:
            temp = numlist[i]
    return temp


print(find_greatest(sample))


