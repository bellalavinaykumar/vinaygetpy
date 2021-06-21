#loops
#while loop
#for loop
#nested loops

def while_loop(n,n1):
    i=n
    while i>=1:
        print("nested ",end="")
        j=n1
        while j>=1:
            print("loop",end=" ")
            j-=1
        print()
        i-=1
while_loop(4,1)
