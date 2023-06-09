a=[6,5,3,4,8,7,7]
print(*a)                             

for i in range(len(a)-1):
   min_max_index=i
   for j in range(i+1, len(a)):
     if a[j]<a[min_max_index]:
       min_max_index=j
   a[min_max_index], a[i]=a[i], a[min_max_index]  
              
  
print (*a)