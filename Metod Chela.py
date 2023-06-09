a=[6,5,3,4,8,7,7]
step=len(a)//2
print(*a)                             
while step>0:
 for i in range(step, len(a)):
   index_to_check=i-step
   while i>0 and a[index_to_check]>a[i]:
     a[i], a[index_to_check]=a[index_to_check], a[i]
     i-=step
     index_to_check-=step
   
 step=step//2 

   
print (*a)