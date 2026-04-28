myfamily={"Child1":{"Name":"Anish","Age":18,"Year":2007},
          "Child2":{"Name":"Anurag","Age":14,"Year":2011}}
print(myfamily)
print(myfamily["Child1"]["Name"])
print(myfamily["Child1"]["Age"])
print(myfamily["Child2"]["Name"])
print(myfamily["Child2"]["Year"])
x=child1={"Name":"Anish","Age":18,"Year":2007}
for x,object in myfamily.items():
    print(object["Name"])
    for y,object in myfamily.items():
        print(object["Age"])
'''
OUTPUT:-
{'Child1': {'Name': 'Anish', 'Age': 18}}
Anish
18
Anurag
14
'''