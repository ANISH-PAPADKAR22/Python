
marks={}
n=int(input("Enter the no of key and values"))
for i in range(n):
    subject=input("Enter the key")
    score=int(input("Enter the score"))
    marks[subject]=score
print(marks)

'''
OUTPUT:-
Enter the no of key and values 1
Enter the key Anish
Enter the score65
{' Anish': 65}
Enter a key to update Anish
Enter the new value 75
Key updated successfully
updated dictionary is: {' Anish': 75}
'''