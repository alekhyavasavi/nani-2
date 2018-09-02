n=int(raw_input())
k=0
for i in range(2,n//2+1):
    if(n%i==0):
       k=k+1
if(n<=0):
     print("yes")
else:
    print("no")
