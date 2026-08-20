# add a new element to a tuple by creating new tuple
x =(10,20,30,40,50)
y =list(x)
y.append(60)  #add new element to the list
x=tuple(y)
print(x)