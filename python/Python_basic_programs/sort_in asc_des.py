#sort the elements in ascending and desecening order 
t5 = (12,31,10,5,45,78,2,67,34)
print("Before Sorting: ",t5)
f = list(t5)
f.sort()      #ascending order
t5 =tuple(f)
print("After Sorting: ",t5)
print(t5[::-1])  #reverse order
print(type(t5))