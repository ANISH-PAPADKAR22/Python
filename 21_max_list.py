numbers=[10,20,50,40]
print("Max numbers",max(numbers))
print("Min numbers",min(numbers))
print("total Sum:",sum(numbers))
'''
OUTPUT:-
Max numbers 50
Min numbers 10
total Sum: 120
'''
'''
INTERACTIVE-IDLE SHELL 
list=[]
list.append(1)

list=[]
list
[]
list.append(1)
list
[1]
list 1=[1,5,6,7,10]
SyntaxError: invalid syntax
list=[1,5,6,7,10]
list
[1, 5, 6, 7, 10]
 ==============================
[1, 5, 6, 7]
#list comprehend
b=list(x*x for x in l1)
b
[1, 25, 36, 49]
evwen=[]
even=[]
even=list(x for x in range(1,100)
          if x%2==0)
even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

odd=list(x for x in range(1,100)
          if x%2!=0)
odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

'''
