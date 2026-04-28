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
s : 26
t : 26
h : 24
y : 22
k : 11
w : 11
m : 11
f : 11
n : 11
g : 11
i : 4

 : 2
p : 2
a : 2
b : 2

Word Frequencies : Gadhe is good boy
  : 3
o : 3
g : 2
d : 2
a : 1
h : 1
e : 1
i : 1
s : 1
b : 1
y : 1
'''