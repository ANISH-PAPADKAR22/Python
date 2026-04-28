try:                        #error is probable and it should provide some texts
    file = open("example.txt","r")
    text = file.read()
    file.close()
    
    d_file = open("anish.txt","w")
    d_file.write(text)
    d_file.close()
    print("File copied successfully")

    d_file = open("anish.txt","r")
    content = d_file.read()
    print(content)

except FileNotFoundError:                       #INBUILD 
    print("Error:Source does not Exist")

except Exception as e:                          #
    print("An Unexpected error occured")

'''
OUTPUT:-
File copied successfully
yash is noob 

File copied successfully
yash is noob and ashu is bot 

Error:Source does not Exist
'''
