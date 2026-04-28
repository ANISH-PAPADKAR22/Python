class Employee:

    #Constructor
    def __init__(self,emp_id,name,salary):
        self_emp_idd = emp_id
        self.name = name
        self.salary = salary
        print("Employee{self.name}created")

    #Methods to display details
    def display(self):
        print("Employee details")
        print("ID,self_emp_id")
        print("Name,self.name") 
        print("Salary,self.salary")
    
    #Destructor
    def __del__(self):
        print(f"Employee{self.name}deleted")

#Creating objects of Employee class
emp1 = Employee(101,"Anish",60000)
emp2 = Employee(102,"Ashutosh",69000)

#Display details
emp1.display
emp2.display

#Deleting Objects
del emp1
del emp2