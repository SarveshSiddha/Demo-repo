a=int(input("enter the number"))
demo=a
rev=0
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(demo==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")
