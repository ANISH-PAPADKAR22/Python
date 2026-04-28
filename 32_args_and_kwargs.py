    #Demonstrate the use of *args and **kwargs in Python functions.
def demo(*args, **kwargs):
        print("Arguments passed using *args:", args)
        print("Arguments passed using **kwargs:", kwargs)
    demo(10,20,30,name = "DjAlok", City = "Pune")

def stud_info(*args, **kwargs):
        print("Subjects:")
        for student in args:
            print(student)
        print("Student Details:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    subjects = input("Enter the subjects: ").split()
    name = input("Student name: ")
    age = input("Student age: ")
    city = input("Student city: ")
    stud_info(*subjects, name=name, age=age, city=city)

    '''
    OUTPUT:-
    Enter the subjects: ctp
    Student name: Gadhe
    Student age: 18
    Student city: pune
    Subjects:
    ctp
    Student Details:
    name: Gadhe
    age: 18
    city: pune
    '''