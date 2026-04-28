class Demo:
    def __init__(self, name):
        self.name = name
        print(f"{self.name}created")

    def __del__(self):
        print(f"{self.name}destroyed")

obj = Demo("Object1")
del obj
'''
OUTPUT:-
Object1created
Object1destroyed
'''