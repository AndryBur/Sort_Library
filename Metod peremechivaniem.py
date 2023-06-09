a=[6,5,3,4,8,7,7]
left_index=0
right_index=len(a)-1
print(*a)                             
while left_index<=right_index:
   
   for i in range(left_index, right_index):
      if a[i]>a[i+1]:
         a[i],a[i+1]=a[i+1],a[i]
   right_index-=1
   
   for i in range(right_index, left_index,-1):   
      if a[i]<a[i-1]:
         a[i],a[i-1]=a[i-1],a[i]
   left_index+=1                         
  
print (*a)