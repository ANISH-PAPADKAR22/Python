class student:

    def setstudent(self):
        self.roll_no = int(input("Enter the roll no of the student"))
        self.name = input("Enter the name of student")
        self.mark1 = int(input("Enter the marks of CTP"))
        self.mark2 = int(input("Enter the marks of PSP"))
        
    def printstudent(self):
        print(self.roll_no)
        print(self.name)
        print(self.mark1)
        print(self.mark2)
        
s1 = student()
s1.setstudent()
s1.printstudent()

s2 = student()
s2.setstudent()
s2.printstudent()
print(id(s1))
print(id(s2))

'''
OUTPUT:-
Enter the roll no of the student 2
Enter the name of studentDiva
Enter the marks of CTP20
Enter the marks of PSP21
2
Diva
20
    21
Enter the roll no of the student5
Enter the name of studentgadhe
Enter the marks of CTP25
Enter the marks of PSP26
5
gadhe
25
2679364161552
2679357414560
'''

        
        
