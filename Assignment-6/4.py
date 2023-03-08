#4. Write a Python program to check a triangle is equilateral, isosceles or scalene.


x=int(input(""))
y=int(input(""))
z=int(input(""))

if x==y==z:
    print("Equilateral Triangle")
elif x==y or x==z or y==z:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")
