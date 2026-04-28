numbers = [10,11,15,20,37,30,35,40]
even_numbers = list(filter(lambda x:x%2 == 0,numbers)) #lambda = Temporary variable decln
odd_numbers = list(filter(lambda x:x%2!= 0,numbers))
print("Orignal List",numbers)
print("Even Numbers",even_numbers)
print("Odd Numbers",odd_numbers)
'''
Output:
Orignal List [10, 15, 20, 35, 30, 35, 40]
Even Numbers [10, 20, 30, 40]
Odd Numbers [11, 15, 37, 35]
'''
