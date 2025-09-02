#Write a program that asks for the base and height of a rectangle. The program prints the perimeter and area of the  rectangle. The perimeter of a rectangle is the sum of the lengths of its four sides.

base = float(input("Please enter the base of a rectangle: "))
height = float(input("Please enter the height of a rectangle: "))
perimeter = 2*base + 2*height
area = base*height
print(f"The perimeter of the rectangle is : {perimeter:5.2f} and the area of the rectangle is : {area:5.2f}")
