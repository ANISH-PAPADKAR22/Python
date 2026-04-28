class Dog:
    def sound(self):
        print("Dog Barks")
class Cat:
    def sound(self):
        print("Cat Meows")

for animal in (Dog(), Cat()):
    animal.sound() 