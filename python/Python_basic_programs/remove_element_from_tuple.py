#1.removing element from tuple by converting it into list
t1 = (10,20,30,40,50)
li =list(t1)   #converting the tuple to list
print(type(li))
li.remove(30) 
t1 = tuple(li)  #converting list to tuple
print(t1)
print(type(t1))
