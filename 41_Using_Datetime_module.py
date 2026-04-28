from datetime import datetime
now = datetime.now()  # Get the current date and time
print("Current Date and Time:", now)

date1 = datetime(2007,9,22)
date2 = datetime(2011,9,22)

difference = date2 - date1
print("Difference:",difference)