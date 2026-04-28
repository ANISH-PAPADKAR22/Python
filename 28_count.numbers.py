SI="My number is 425678489"
count=0
for char in SI:
    #if char.isdigit():
    #if char.isalpha():
    if char.isalnum():
        count+=1
    
print("The number of digits in the string is:", count)
#OUTPUT:-The number of digits in the string is: 9
#OUTPUT:-The number of digits in the string is: 10
#OUTPUT:-The number of digits in the string is: 19