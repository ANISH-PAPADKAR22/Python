def create_newfile():
    print("Creating a new file: ")
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents")
    with open(file_name, "w") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

def read_mode():
    print("Opening file in read mode")
    file_name = input("\nEnter file name: ")
    print("The file contents are as follows: ")
    print("------------------------------------")
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
        file.close()
    print("---------End of File-----------")

def append_mode():
    file_name = input("\nEnter file name: ")
    file_content = input("\nStart typing the contents")
    with open(file_name, "a") as file:
        file.write(file_content)
        file.close()
    print("File written successfully")

while(True):
    print("Menu:")
    print("1. Create a new file,fiel in write mode and write into it")
    print("2. Reopen file in read mode and dislpay the content")
    print("3. reopen the file in appemnd mode and write into it")
    print("4. Open the file in read mode and count the frequency of each word")
    print("5. Exit")
    print("************************")
    ch = int(input("Enter your choice"))
    if ch == 1:
        create_newfile()
    elif ch == 2:
        read_mode()
    elif ch == 3:
        append_mode()
    elif ch == 4:
    #   Count the frequency of each word
        count_word_freq()
    elif ch == 5:
        break
    else:
        print("Wrong Choice! Try Again")
print("Exiting the program...")


'''
OUTPUT:
1. Create a new file,fiel in write mode and write into it
2. Reopen file in read mode and dislpay the content
3. reopen the file in appemnd mode and write into it
4. Open the file in read mode and count the frequency of each word
5. Exit
************************
Enter your choice 1
Creating a new file: 

Enter file name: anish.txt

Start typing the contents kowhfiuiehuajfiad
File written successfully
Menu:
1. Create a new file,fiel in write mode and write into it
2. Reopen file in read mode and dislpay the content
3. reopen the file in appemnd mode and write into it
4. Open the file in read mode and count the frequency of each word
5. Exit
************************
Enter your choice2
Opening file in read mode

Enter file name: anish.txt
The file contents are as follows: 
------------------------------------
 kowhfiuiehuajfiad
---------End of File-----------
'''