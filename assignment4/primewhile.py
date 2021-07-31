num=int(input("enter the number"))
i=2
flag=0
while (i<=num//2):
    if (num%i==0):
        flag=flag+1
    i=i+1
if flag==0 and num!=1:
    print("prime")
else:
    print("no prime")
