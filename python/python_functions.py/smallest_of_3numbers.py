def smallest(a,b,c):
    if(a<c and a<b):
        print("Smallest number is:",a)
    elif(b<a and b<c):
        print("Smallest number is:",b)
    else:
        print("Smallest number is:",c)    
smallest(12,10,18)