a=int(input("enter the number"))
if a>1:
    for i in range(2,a):
        if a % i == 0:
           print("it is a not prime number")
           break
        else:
           print("it is a prime number")
           break
else:
   print("it is a not prime number")
    
