n=int(input("enter the number"))
c=n
print("value of c is ",c)
a=n%10
print("value of a is ",a)
n=n//10
print("value of n is",n)
b=n%10
print("value of b is",b)
n=n//10
print("value of new n is ",n)


if ((a*a*a)+(b*b*b)+(n*n*n)==c):
    print("armstrong")
else:
    print("no armstrong")
