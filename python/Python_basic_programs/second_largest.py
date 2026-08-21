# Finding the second largest number in the tuple
s1 = (12,21,45,32,10,39)
largest = 0    
second  = 0
for x in s1 :
    if x > largest:
        second = largest
        largest = x
    elif x > second:
      second  = x
print("The Second Largest Number: " ,second) 