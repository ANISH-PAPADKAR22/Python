marks={}
n=int(input("Enter the no of key and values"))
for i in range(n):
    subject=input("Enter the key")
    score=int(input("Enter the score"))
    marks[subject]=score
print(marks)
new_key=input("Enter a key to update")
if new_key in marks:
    new_value=int(input("Enter the new value"))
    #marks[new_key]=new_value
    marks.update({new_key:new_value})
    print("Key updated successfully")
else:
    print("Key Not found")
print("updated dictionary is:",marks)
'''
1st OUTPUT:-(    #marks[new_key]=new_value
)
Enter the no of key and values 1
Enter the key Anish
Enter the score65
{' Anish': 65}
Enter a key to update Anish
Enter the new value 75
Key updated successfully
updated dictionary is: {' Anish': 75}
'''
'''
2nd OUTPUT:-(marks.update({new_key:new_value}))
Enter the no of key and values 2
Enter the keyAnish
Enter the score95
Enter the keyAnurag
Enter the score90
{'Anish': 95, 'Anurag': 90}
Enter a key to updateAnurag
Enter the new value99
Key updated successfully
updated dictionary is: {'Anish': 95, 'Anurag': 99}'''