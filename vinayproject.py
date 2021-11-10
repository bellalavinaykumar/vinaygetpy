list=(1,2,3,4,5,6,7,8,9)
odd_count=0
even_count=0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f'Total Odd Numbers Present in list {odd_count} ')
print(f'Total even Numbers Present in list {even_count} ')
