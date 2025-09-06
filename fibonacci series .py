def fibonacci(n):
    a,b=0,1
    print(a)
    print(b)
    for i in range(n):
        c=a+b
        print(c)
        a,b=b,c

n= int(input("Enter a number of range:"))
fibonacci(n)
