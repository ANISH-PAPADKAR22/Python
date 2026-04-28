set1 = {10,20,30,40}
set2 = {50,60,30,80}
#Union
A = set1 | set2
print(A)

'''
OUTPUT:-
{70, 40, 10, 80, 50, 20, 60, 30}
'''

#Intersection
B = set1 & set2
print(B)

'''
OUTPUT:-
{40, 10, 80, 50, 20, 60, 30}
{30}
'''

#Difference
C = set2 - set1
D = set1 - set2
print(C)
print(D)

'''
OUTPUT:-
{80, 50, 60}
{40, 10, 20}
'''

#Symmetric Difference
E= set1 ^ set2
print(E)
'''
OUTPUT:-
{40, 10, 80, 50, 20, 60}
'''

#Subset and Superset
F=set1.issubset(set2)
G=set1.issuperset(set2)
print(F)
print(G)
'''
OUTPUT:-
False
False
'''

#Set into listConversion
List=list(set1)
print(List)
'''
OUTPUT:-
[40, 10, 20, 30]
'''

#List into set Conversion
Set=set(List)
print(Set)

'''
OUTPUT:_
{40, 10, 20, 30}
'''

find=70
set1 = list(set1)
for num in set1:
    if num==find:
        print("This number is present")
        break
    else:
        print("This number is not present")
        break

'''
OUTPUT:-
This number is not present
'''
