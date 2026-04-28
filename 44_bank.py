class employee:
    def setemployee(self):
        self.name = input("Enter your name")
        self.id = int(input("Enter your id"))
        self.salary = int(input("Enter your salary"))
    def printemployee(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Salary:", self.salary)

e1 = employee()
e1.setemployee()
e1.printemployee()

e2 = employee()
e2.setemployee()
e2.printemployee()
'''
OUTPUT:-
Enter your name Anish
Enter your id 4825
Enter your salary 60000 
Name:  Anish
ID: 4825
Salary: 60000
Enter your name Ashutosh
Enter your id 4826
Enter your salary 69000
Name:  Ashutosh
ID: 4826
Salary: 69000
'''