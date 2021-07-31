lst = []
a=int(input("how many number : "))
for n in range(a):
    number = int(input("enter the number "))
    lst.append(number) #using append we are add new element at last position
print("sum of all elements is : ",sum(lst))
