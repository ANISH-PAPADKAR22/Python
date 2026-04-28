#Find the area of triangle,rectangle and circle
#For Triangle
Base_triangle=int(input("Enter the base of the triangle:"))
Height_triangle=int(input("enter the height of the triangle:"))
area=(Base_triangle+Height_triangle)/2
print("The area of the triangle is:",area)
#For rectangle
length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
area=length*breadth
print("The area of the rectangle is:",area)
#For circle
radius=float(input("Enter the radius of the circle:"))
area=3.14*radius**2
print("The area of the circle is:",area)
'''
Output:-
Enter the base of the triangle:20
enter the height of the triangle:20
The area of the triangle is: 20.0
Enter the length of the rectangle:30
Enter the breadth of the rectangle:25
The area of the rectangle is: 750
Enter the radius of the circle:5
The area of the circle is: 78.5
'''
