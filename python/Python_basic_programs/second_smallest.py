#Finding the second smallest number in the tuple
s2= (12,21,45,32,10,39)
largest = 0    
second  = 0
for x in s2 :
    if x < largest:
        second = largest
        largest = x
    elif x > second:
      second  = x
print("The Second Smallest Number: ",second) 