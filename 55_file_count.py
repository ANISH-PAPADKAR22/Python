#cREATE A FILE AND COUNT THE NUMBER OF TIMES EACH IP ADDRESS APPEARS IN THE FILE
#WRITE A PROGRAM TO EXTRACT UNIQUE IP ADDRESSES AND COUNT THEIR OCCURRENCES
file = open("access.log","w")
file.write("2036-04-15 192.168.1.1 /home\n")
file.write("2036-04-15 192.168.1.2 /about\n")
file.write("2036-04-15 192.168.1.1 /contact\n")

from collections import Counter

file = open("access.log","r")
lines = file.readlines()
file.close()

ips = []

for line in lines:
    parts = line.split()
    ips.append(parts[1])

unique_ips = set(ips)
print("Unique IPs:", unique_ips)

ip_count = Counter(ips)
print("\nIP Add ress count:")
for ip, count in ip_count.items():
    print(ip, ":", count)

'''OUTPUT:-
IP addresses count:
192.168.1.1: 2
192.168.1.2: 1

IP addresses count:
192.168.1.4: 1
192.168.1.2: 1
192.168.1.1: 1
'''