import random

arr=[]
while len(arr) < 10:
    arr.append(random.randint(0, 100))
    
for i in arr:
    print(str(i)+' ')

print("\n")

if arr == sorted(arr):
    print("True\n")
else:
    print("False\n")

iss = input("Do you want to sort this list? Y/N: ")
if iss == 'Y' or iss == 'y':
    arr.sort()
else:
    exit()

for i in arr:
    print(str(i)+' ')

print("\n")

if arr == sorted(arr):
    print("True\n")
else:
    print("False\n")

exit()
