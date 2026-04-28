def display_info(*args,**kwargs):
    print("Arguments:",args)
    print("Keyword Arguments:",kwargs)

display_info(10, 20, 30, name = "Modi", role = "PM")
'''
OUTPUT:-
Arguments: (10, 20, 30)
Keyword Arguments: {'name': 'Modi', 'role': 'PM'}
'''
