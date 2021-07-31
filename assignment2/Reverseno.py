n=int(input("enter the num"))
rev=0
while(n>0):
    rev=rev*10
    rev=rev+n%10
    n=n/10
print("reverse no is : ",rev)
