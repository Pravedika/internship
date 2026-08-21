#finding number of even and odd numbers present in a tuple
count1 = 0  
count2 = 0
t9 = (2,16,4,8,1,3,19,5)
for x in t9:
    if x % 2 == 0:
     count1 += 1
    else:
       count2 += 1
print("even numbers count: ",count1)
print("odd numbers count",count2)