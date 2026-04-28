data={}
n=int(input("Enter the number of key and values"))
for i in range(n):
    key=input("Enter the key")
    value=input("Enter the value")
    data[key]=value
print(data)

'''
OUTPUT:-
Enter the number of key and values2
Enter the key6
Enter the value5
Enter the key2
Enter the value6
{'6': '5', '2': '6'}
'''