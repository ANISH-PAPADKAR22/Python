#Create and write the file
file = open("example.txt","a")
file.write("Yookoso Welcome to School of Technology")

#Read File
file = open("example.txt","r")
print("Initial content:\n",file.read())
file.close()

#Append New Line
file = open("example.txt","a")
file.write("\nThis is CTPL lab")
file.close()

#Read UPdated File
file = open("example.txt","r")
print("\nUpdates Content:\n",file.read())
file.close()