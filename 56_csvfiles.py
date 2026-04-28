#Write CSV files
import csv

with open("data.csv", "w", newline ="") as file:  #newline is used to avoid blank lines in csv file
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "ID"])
    writer.writerow(["Alice", 30, "1"])
    writer.writerow(["Bob", 25, "2"])
    writer.writerow(["Charlie", 27, "3"])
    writer.writerow(["David", 22, "4"])

#Read CSV file
print("CSV Content:")
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Search ID
search_id = input("enter the Id to search: ")

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    found = False
    for row in reader:
        if row[2] ==search_id:
            print("Record Found:", row)
            found = True
            break
    if not found:
        print("Record Not Found")

'''
OUTPUT:-
CSV Content:
['Name', 'Age', 'ID']
['Alice', '30', '1']
['Bob', '25', '2']
['Charlie', '27', '3']
['David', '22', '4']
enter the Id to search: 2
Record Found: ['Bob', '25', '2']
'''    