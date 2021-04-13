from array import *

arr1=array("i",[])

n=int(input("enter the length of array : "))

for i in range(n):
  k=int(input("enter the value of array : "))
  arr1.append(k)
print(arr1)

num_search=int(input("enter the search value : "))

a=0
for i in arr1:
  if num_search==i:
    print(a)
  a+=1