
def printing_prime(k):
    for i in range(2,k):
        if k%i==0:
            print("not prime")
            break
    else:
        print("prime")

prime=[]
not_prime=[]
n=int(input("enter the num : "))
for i in range(1,n+1):
    if i==1:
        not_prime.append(i)
        continue
    for j in range(2,i):
        if i%j==0:
            not_prime.append(i)
            break
    else:
        prime.append(i)
print(prime)
print(not_prime)