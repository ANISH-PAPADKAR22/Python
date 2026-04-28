#Write a function that accepts any number of arguments and returns the sum and average of those numbers.
'''def sum_avg(*args):
    total = 0
    avg = total/len(args)
    for num in args:
        total+=num
        avg = total/len(args)
    return total
print("sum is :", sum_avg(5, 15))
print("average is:", sum_avg(5, 15)/2)

OUTPUT:-
sum is : 20
average is: 10.0
'''
def sum_avg(*args):
    total = 0
    avg = total/len(args)
    return args
num = int(input("Enter the number of elements: "))
num_list = list(map(int, input("Enter the numbers: ").split()))
result = sum_avg(*num_list)
print("Sum is:", result)
'''
OUTPUT:-
Enter the number of elements: 3
Enter the numbers: 1 2 3
Sum is: (6, 2.0)
'''
'''
OUTPUT:-
Enter the number of elements: 3 
Enter the numbers: 1 2 3 
Sum is: (1, 2, 3)
'''