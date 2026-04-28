#Base Class
class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

#Derived Class
class Employee(Person):
    def __init__(self, name, age, emp_id,department):
        super().__init__(name, age)        #
        self.emp_id = emp_id
        self.department = department

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}, Department: {self.department}")

#Further class
class Manager(Employee):
    def __init__(self, name, age, emp_id, department, team_size):
        super().__init__(name, age, emp_id, department) #super() is used to call the constructor of the parent class (Employee) to initialize the inherited attributes (name, age, emp_id, department)
        self.team_size = team_size

    def display_manager(self):
        print(f"Team Size: {self.team_size}")

#Demonstration
manager = Manager("Alex" , 24 , "G105" , "11" , 10)

#Using methods for all the levels
manager.display_person()      #From Person class 
manager.display_employee()    #From Employee class
manager.display_manager()     #From Manager class   
'''
OUTPUT:-
Name: Alex, Age: 24
Employee ID: G105, Department: 11
Team Size: 10
'''