import math

def getArea(shape):
    shape = shape.lower()
    if shape == "r":
        rectangleArea()
    elif shape == "c":
        circleArea()
    elif shape == "t":
        triangleArea()
    else:
        print("Please enter 'r', 'c' or 't' ")
        return main()
def rectangleArea():
    try:
        lenght = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = lenght*width
        print("The area of the rectangle is: {:.2f}".format(area))
    except ValueError:
        print("Please enter a number")
        return rectangleArea()
def circleArea():
    try:
        radius = float(input("Enter the radius: "))
        area = math.pi * (math.pow(radius,2))
        print("The area of the circle is: {:.2f}".format(area))
    except ValueError:
        print("Please enter a number")
        return circleArea()
def triangleArea():
    try:
        height = float(input("Enter the height: "))
        base = float(input("Enter the base: "))
        area = height * base / 2
        print("The area of the triangle is: {:.2f}".format(area))
    except ValueError:
        print("Please enter a number")
        return triangleArea()
def main():
    type_of_shape = input("R for Rectangle\nC for Circle\nT for Triangle\nEnter the shape type: ")
    getArea(type_of_shape)
main()