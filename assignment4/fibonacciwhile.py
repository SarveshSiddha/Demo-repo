number=int(input("enter the value "))
n1=0
n2=1
count=0
if number<=0:
    print("enter positive value")
elif number==1:
    print("Fibonacci series upto ",number," : ")
    print(n1)
else:
    print("Fibonacci sequence ")
    while count<number:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
