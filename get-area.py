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
    lenght = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = lenght*width
    print("The area of the rectangle is: {:.2f}".format(area))
def circleArea():
    radius = float(input("Enter the radius: "))
    area = math.pi * (math.pow(radius,2))
    print("The area of the circle is: {:.2f}".format(area))
def triangleArea():
    height = float(input("Enter the height: "))
    base = float(input("Enter the base: "))
    area = height * base / 2
    print("The area of the triangle is: {:.2f}".format(area))

def main():
    type_of_shape = input("Enter the shape type\nr for rectangle\nc for circle\nt for triangle\n")
    getArea(type_of_shape)
main()