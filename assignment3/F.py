#print F using *
for i in range(0,6):
    for j in range(0,5):
        if i==0 or i==2 or j==0:
            print("*",end='');
        else:
            print(" ",end='')
    print("");
    
