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
