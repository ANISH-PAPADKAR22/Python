str=input("Enter the string")
vowel=0
consonant=0
for ch in str:
    if (ch=='a' | ch=='e' | ch=='i' | ch=='o' | ch=='u' | ch=='A' | ch=='E'\
        | ch=='I' | ch=='O' | ch=='U'):
        vowel+=1
    elif(ch>='a' and ch<='z')|(ch>='A' and ch<='Z'):

        consonant+=1
print("No of vowels are:",vowel)
print("No of consonant are:",consonant)
'''
OUTPUT:-
Enter the string divakar
No of vowels are: 3
No of consonant are: 4

Traceback (most recent call last):
  File "/usr/lib/python3.12/idlelib/run.py", line 580, in runcode
    exec(code, self.locals)
  File "/home/str/vow_con_11.py", line 5, in <module>
    if (ch=='a' | ch=='e' | ch=='i' | ch=='o' | ch=='u' | ch=='A' | ch=='E'\
            ~~~~^~~~
TypeError: unsupported operand type(s) for |: 'str' and 'str'
Python interprets this expression from left to right. When it reaches ch == a | ch == e, it first evaluates ch == a (which results in a boolean True or False).
It then tries to apply the bitwise OR operator (|) between that boolean and the string 'ch == e'.
The bitwise operator expects integer operands, which causes the TypeError when it encounters strings or booleans in this manner
'''
