string=input("enter the String")
a=["a","e","i","o","u"]
v=0
c=0
string=string.lower()
for s in string:
    if s in a:
        v+=1
    elif s==" ":
        i=1
    else:
        c+=1
print(f"vowels: {v}")
print(f"consonent: {c}")
'''
OUTPUT:-
enter the String akhilesh
vowels: 3
consonent: 5

enter the String anish
vowels: 2
consonent: 3
'''
