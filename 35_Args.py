def add_numbers(*args):  #Arguments are stored in tuple
    print(args)
    print("Sum:",sum(args))


add_numbers(10.6,20,31.2)

'''
OUTPUT:-
(10, 20, 30)
Sum: 60

(10.6, 20, 31.2)
Sum: 61.8
'''
