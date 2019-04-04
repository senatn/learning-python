import random

list = []

for i in range(6):
    list.append(random.randrange(1,15))

print("List of random numbers: {} ".format(list))

def bubbleShort(list):
    n = len(list) - 1
    for i in range(n):
        for j in range(n-i):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
    return list

print("\nList of random numbers but now all of them in a order: {} ".format(bubbleShort(list)))