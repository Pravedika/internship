#1.removing element from tuple by converting it into list
t1 = (10,20,30,40,50)
li =list(t1)   #converting the tuple to list
print(type(li))
li.remove(30) 
t1 = tuple(li)  #converting list to tuple
print(t1)
print(type(t1))
#2.replace the value
t2 = (11,22,33,43,53)
l =list(t2)   #converting the tuple to list
print(type(l))
l[2]=70        
t2 = tuple(l)  #converting list to tuple
print(t2)
#3.taking user input to insert values into the tuple
n = int(input("enter the value: "))
x = []
x.append(n)
y =tuple(x)
print(y)
print(type(y))
#4.check type of tuple
o =tuple()
print(type(o))
#5.displaying the data by using for loop
t3 = ("pravedika","abhi","mohith","praneeth")
print(t3)
#6.sorting the elements 
t4 = (34,76,87,44,85,90)
l2 = list(t4)
l2.sort()
t4 = tuple(l2)
print(t4[-1])
#7.find the sum of numbers
sum = 0
avg = 0
for x in t1:
    sum += x
print(sum) 
#8.finding the average of numbers  
for x in t4:
    sum += x
    avg = sum/len(t1) 
print(avg)  
#9.sort the elements in ascending and desecening order 
t5 = (12,31,10,5,45,78,2,67,34)
print("Before Sorting: ",t5)
f = list(t5)
f.sort()      #ascending order
t5 =tuple(f)
print("After Sorting: ",t5)
print(t5[::-1])  #reverse order
print(type(t5))
# 10.Finding the second largest number in the tuple
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
# 11.Finding the second smallest number in the tuple
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
# 12.finding number of even and odd numbers present in a tuple
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
# 13.Displaying each user name by using for loop
g1 = ("pravee","mohith","abhi")
for x in g1:
 print(x)
#14. Displaying Even Numbers
g2 = (12,78,33,19,7,455,32,16)
for x in g2:
  if x % 2 == 0:
   print(x)
#15.Displaying Odd Numbers
g2 = (12,78,33,19,7,455,32,16)
for x in g2:
  if x % 2 != 0:
   print("Odd numbers: ",x)
#16.displaying user data
t = (("name:","pravedika"),("branch:","CSE"),("course:","Python Full Stack"))     
for x in t:
   print(x[0],x[1])   