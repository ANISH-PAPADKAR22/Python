#To calculate employees gross salary
basic_salary=float(input("Enter the basic salary: "))
da=0.5*basic_salary
hra=0.2*basic_salary
gross_salary=basic_salary+hra+da
print("The Dearness allowance is :",da)
print("The House Rent Allowance is :",hra)
print("The Gross salary of the Employee is:",gross_salary)
'''
Output:-
Enter the basic salary: 60000
The Dearness allowance is : 30000.0
The House Rent Allowance is : 12000.0
The Gross salary of the Employee is: 102000.0
'''