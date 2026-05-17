# ============================================================
# REMEMBER.PY - All Important Python Concepts Merged
# ============================================================

# ============================================================
# 1. SALARY CALCULATION (from 3_Salary.py)
# ============================================================
#To calculate employees gross salary
basic_salary = float(input("Enter the basic salary: "))
da = 0.5*basic_salary
hra = 0.2*basic_salary
gross_salary = basic_salary+hra+da
print("The Dearness allowance is :",da)
print("The House Rent Allowance is :",hra)
print("The Gross salary of the Employee is:",gross_salary)
'''
Output:-
Enter the basic salary: 60000
The Dearness allowance is : 30000.0
The House Rent Allowance is : 12000.0
The Gross salary of the Employee is: 102000.0
'''



# ============================================================
# 2. MEAN, MEDIAN, MODE (from 42_Using_stats_module.py)
# ============================================================
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Mean:", statistics.mean(data))  # mean():Average of the data
print("Median:", statistics.median(data))  # median():Middle value of the data
print("Mode:", statistics.mode(data))  # mode():Most common value in the data

'''
OUTPUT:-
Mean: 5.5
Median: 5.5
Mode: 1
'''


# ============================================================
# 3. FILE HANDLING (from 51_fileHandling.py & 52_FH2.py)
# ============================================================
#Create and write the file

file = open("example.txt","a")
file.write("Yookoso Welcome to School of Technology and Research")

#Read File
file = open("example.txt","r")
print("Initial content:\n",file.read())
file.close()

#Append New Line
file = open("example.txt","a")
file.write("\nThis is CTPL lab")
file.close()

#Read UPdated File
file = open("example.txt","r")
print("\nUpdates Content:\n",file.read())
file.close()

# --- Menu-based File Handling (from 52_FH2.py) ---
def create_newfile():
    print("Creating a new file: ")
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents")
    with open(file_name, "w") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

def read_mode():
    print("Opening file in read mode")
    file_name = input("\nEnter file name: ")
    print("The file contents are as follows: ")
    print("------------------------------------")
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
        file.close()
    print("---------End of File-----------")

def append_mode():
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents")
    with open(file_name, "a") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

def count_word_freq():
    file_name = input("\nEnter file name: ")
    with open(file_name, "r") as file:
        content = file.read().lower()
    words = content.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print("Word Frequencies:")
    for word, count in freq.items():
        print(f"  '{word}' : {count}")

while(True):
    print("Menu:")
    print("1. Create a new file,fiel in write mode and write into it")
    print("2. Reopen file in read mode and dislpay the content")
    print("3. reopen the file in appemnd mode and write into it")
    print("4. Open the file in read mode and count the frequency of each word")
    print("5. Exit")
    print("************************")
    ch = int(input("Enter your choice"))
    if ch == 1:
        create_newfile()
    elif ch == 2:
        read_mode()
    elif ch == 3:
        append_mode()
    elif ch == 4:
    #   Count the frequency of each word
        count_word_freq()
    elif ch == 5:
        break
    else:
        print("Wrong Choice! Try Again")
print("Exiting the program...")


# ============================================================
# 4. EXCEPTION HANDLING (New Code)
# ============================================================
# ZeroDivisionError

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")

# IndexError
try:
    lst = [1, 2, 3]
    index = int(input("Enter index to access (list has 3 elements): "))
    print("Element at index", index, ":", lst[index])
except IndexError:
    print("Error: Index out of range!")

# KeyError
try:
    d = {"name": "Alice", "age": 25}
    key = input("Enter key to access (available: name, age): ")
    print("Value:", d[key])
except KeyError:
    print("Error: Key not found in dictionary!")

# FileNotFoundError
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")

# Finally block
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Error: Invalid input!")
finally:
    print("This block always executes (finally block).")

'''
OUTPUT:-
Enter numerator: 10
Enter denominator: 0
Error: Cannot divide by zero!
Enter index to access (list has 3 elements): 5
Error: Index out of range!
Enter key to access (available: name, age): email
Error: Key not found in dictionary!
Error: File not found!
Enter a number: 4
Square: 16
This block always executes (finally block).
'''


# ============================================================
# 5. SETS OPERATIONS (from 23_set_operations.py)
# ============================================================
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


# ============================================================
# 6. SUM OF EVEN NUMBERS (New Code)
# ============================================================
n = int(input("Enter the limit (N): "))

# Method 1: Using loop
total = 0
for i in range(2, n + 1, 2):
    total += i
print("Sum of even numbers from 1 to", n, "(loop):", total)

# Method 2: Using list comprehension
total2 = sum([i for i in range(1, n + 1) if i % 2 == 0])
print("Sum of even numbers from 1 to", n, "(comprehension):", total2)

# Method 3: Using formula
even_count = n // 2
total3 = even_count * (even_count + 1)
print("Sum of even numbers from 1 to", n, "(formula):", total3)

'''
OUTPUT:-
Enter the limit (N): 10
Sum of even numbers from 1 to 10 (loop): 30
Sum of even numbers from 1 to 10 (comprehension): 30
Sum of even numbers from 1 to 10 (formula): 30
'''


# ============================================================
# 7. REVERSE NUMBER (New Code - 7_Reverse.py was empty)
# ============================================================
num = int(input("Enter a number: "))

# Method 1: Using string slicing
reversed_str = str(num)[::-1]
print("Reversed (string method):", reversed_str)

# Method 2: Using loop
original = abs(num)
reversed_num = 0
while original > 0:
    digit = original % 10
    reversed_num = reversed_num * 10 + digit
    original //= 10
print("Reversed (loop method):", reversed_num)

'''
OUTPUT:-
Enter a number: 12345
Reversed (string method): 54321
Reversed (loop method): 54321
'''


# ============================================================
# 8. MATRIX OPERATIONS (New Code)
# ============================================================
# Define two matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# Matrix Addition
rows = len(A)
cols = len(A[0])
addition = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
print("\nAddition (A + B):")
for row in addition:
    print(row)

# Matrix Subtraction
subtraction = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
print("\nSubtraction (A - B):")
for row in subtraction:
    print(row)

# Matrix Multiplication
multiplication = [[sum(A[i][k] * B[k][j] for k in range(cols)) for j in range(cols)] for i in range(rows)]
print("\nMultiplication (A * B):")
for row in multiplication:
    print(row)

# Transpose of A
transpose = [[A[j][i] for j in range(rows)] for i in range(cols)]
print("\nTranspose of A:")
for row in transpose:
    print(row)

'''
OUTPUT:-
Matrix A:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Matrix B:
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]

Addition (A + B):
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]

Subtraction (A - B):
[-8, -6, -4]
[-2, 0, 2]
[4, 6, 8]

Multiplication (A * B):
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]

Transpose of A:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
'''


# ============================================================
# 9. PALINDROME STRING (from 8_palindrome.py)
# ============================================================
#if string is palindrome
s=input("Enter the content")
s.lower() #convert to Lower case
s.upper()#Convert to uppercase
if s==s[::-1]:
 print("It is a  palindrome")
else:
     print("It is not  palindrome")
'''
Output:-
Enter the content anish
It is not  palindrome

Enter the content madam
It is a  palindrome

Enter the content Madam
It is not  palindrome

'''


# ============================================================
# 10. LIST OPERATIONS (from 15_Lists.py & 21_max_list.py)
# ============================================================
#Create a list of numbers
nums=[10,20,30,40]
print("original list",nums)
nums.append(50)
print("new lists",nums)
nums.insert(1,220)           #insert-->(index,number to be inserted
print("New list",nums)
'''
OUTPUT:-
original list [10, 20, 30, 40]
new lists [10, 20, 30, 40, 50]
New list [10, 220, 20, 30, 40, 50]
'''

# Max, Min, Sum (from 21_max_list.py)
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


# ============================================================
# 11. DICTIONARY OPERATIONS (from 24, 25, 26, 27, 29)
# ============================================================

# --- Input Dictionary (from 24_input_dictionary.py) ---
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

# --- Marks Dictionary (from 25_Marks_dictionary.py) ---
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
'''

# --- Key Update (from 26_key_update.py) ---
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

# --- Nested Dictionary (from 29_nested_dictionaary.py) ---
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


# ============================================================
# 12. WORD FREQUENCY (from 27_count to_dictionary.py & 53_FH3.py)
# ============================================================

# --- Character Count in String (from 27_count to_dictionary.py) ---
'''
input
count the occurrence of each character in a string and
display in dictionary'''
file=input("Enter the string")
char_count={}
for char in file:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
print("Character count is:", char_count)
for char, count in char_count.items():
    print(f"Character '{char}' occurs {count} times") 
'''
OUTPUT:-
Enter the string Anish Papadkar
Character count is: {' ': 2, 'A': 1, 'n': 1, 'i': 1, 's': 1, 'h': 1, 'P': 1, 'a': 3, 'p': 1, 'd': 1, 'k': 1, 'r': 1}
Character ' ' occurs 2 times
Character 'A' occurs 1 times
Character 'n' occurs 1 times
Character 'i' occurs 1 times
Character 's' occurs 1 times
Character 'h' occurs 1 times
Character 'P' occurs 1 times
Character 'a' occurs 3 times
Character 'p' occurs 1 times
Character 'd' occurs 1 times
Character 'k' occurs 1 times
Character 'r' occurs 1 times
'''

# --- Word Frequency from File (from 53_FH3.py) ---
from collections import Counter

file = open("example.txt","r")
text = file.read().lower()
file.close()

words = text.split()
word_count = Counter(text)

sorted_words = sorted(word_count.items(),key=lambda x:x[1],reverse = True)

print("Word Frequencies :")

for word,count in sorted_words:
    print(word ,":" ,count)

'''
OUTPUT:-
Word Frequencies :
o : 121
  : 61
l : 37
c : 35
e : 33
'''


# ============================================================
# 13. FACTORIAL USING RECURSION (from 30_Functions.py)
# ============================================================
def add(a, b):
    return a + b

print(add(5, 6))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

square = lambda x:x * x
num = int(input("Input the number:"))
result = (square(num))
print("square of the number is :",result)
'''
Output:-
11
120
'''


# ============================================================
# 14. CSV FILE (from 56_csvfiles.py)
# ============================================================
#Write CSV files
import csv

with open("data.csv", "w", newline ="") as file:  #newline is used to avoid blank lines in csv file
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "ID"])
    writer.writerow(["Alice", 30, "1"])
    writer.writerow(["Bob", 25, "2"])
    writer.writerow(["Charlie", 27, "3"])
    writer.writerow(["David", 22, "4"])

#Read CSV file
print("CSV Content:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Search ID
search_id = input("enter the Id to search: ")

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    found = False
    for row in reader:
        if row[2] ==search_id:
            print("Record Found:", row)
            found = True
            break
    if not found:
        print("Record Not Found")

'''
OUTPUT:-
CSV Content:
['Name', 'Age', 'ID']
['Alice', '30', '1']
['Bob', '25', '2']
['Charlie', '27', '3']
['David', '22', '4']
enter the Id to search: 2
Record Found: ['Bob', '25', '2']
'''
