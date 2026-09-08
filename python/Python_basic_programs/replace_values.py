#replace the value
t2 = (11,22,33,43,53)
l =list(t2)   #converting the tuple to list
print(type(l))
l[2]=70        
t2 = tuple(l)  #converting list to tuple
print(t2)