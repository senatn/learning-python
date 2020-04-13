import random
print("Create and transpose a random matrix!\nPlease enter the following information. ")
row = int(input("Rows\t: "))
column = int(input("Columns\t: "))
From = int(input("From\t: "))
To = int(input("To\t\t: "))
print("\n")

mRandom = [[i for i in (random.randint(From,To) for i in range(column))] for i in range(row)]
for i in mRandom:
    print(i)
print("\n")
TmRandom = [[mRandom[i][j] for i in range(row)] for j in range(column)]
for i in TmRandom:
    print(i)