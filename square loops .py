n= int(input("enter the number for pattern:"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
n=int(input("enter number of rows"))
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end=" ")
    print("\n")