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