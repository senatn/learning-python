square_length = int(input("Length of the square: "))
stars = square_length
spaces = (square_length-2)
lines = square_length-3

for i in range(stars):
    print("*", end="")
print()
for i in range(lines):
    print("*", end="")
    for i in range(spaces):
        print(" ", end="")
    print("*")
for i in range(stars):
    print("*", end="")
    i += 1
print()