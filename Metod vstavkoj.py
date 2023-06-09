a=[6,5,3,4,8,7,7]
print(*a)                             

for i in range(len(a)):
   val=a[i]
   j=i-1
   while val>a[j] and j>=0:
     a[j+1]=a[j]
     j-=1
   a[j+1]=val
              
  
print (*a)