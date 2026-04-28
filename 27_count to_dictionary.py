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