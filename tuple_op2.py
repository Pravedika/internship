t1 = (12,23,34,45,56)
print(t1[0])   #accessing first element in the tuple
print(t1[-1])  #accessing the last element in the tuple
print(t1[2])   #accessing the 3rd element in the tuple
print(t1[0:4])  #acessing elements by using slicing operator
t2 = (12,23,34,40,67,89,67,45,78,90)
print(t2[1:6])  
print(t2[-3:])  #accessing last 3 elements from the tuple
print(t2[1:])   #return all values except 1st value
print(t2[:-1])  #return all elements from tuple except last one
print(t2[::-1])   #return the elements in reverse order
print(t2[0:10:2]) #return elements at even index
# to print elements in alternaive order
for x in t1:
    print(x)
print(t2[1:10:2])   #return the elements at odd index 
print(t2.index(23)) 
print(10 not in t2 )      
t3 = (10,20,30,45,30,23,67,30,43,30)
print(t3.count(30))
t4 = ("java", "c" , "python","mern")
print(t4.index("python"))
t5 =(34,10,45,10,34,10,101,9,10)
print(t5.count(10))
print(t5.index(10))
print("java" in t4)
t6 = t1+t2  #concat the two tuples
print(t6)
t7 =t1*3   #repeat the tuple items 3 times
print(t7)
li =[10,20,30,40,50]
l =tuple(li)
print(l)
print(type(l))
t =(10,23,34,45,56)
p = list(t)
print(p)
print(type(p))
# add a new element to a tuple by creating new tuple
x =(10,20,30,40,50)
y =list(x)
y.append(60)  #add new element to the list
x=tuple(y)
print(x)