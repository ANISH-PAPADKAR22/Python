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