class Parent:
    def show(self):
        print("I am the parent class")
class child(Parent):
    def display(self):
        print("I am the child class")  
obj = child()
obj.show()
obj.display()