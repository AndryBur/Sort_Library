import random

a=[6,5,3,4,8,7,7]
print(*a)                             

def quick_sort(a): 
  if len(a)<=1:
    return a
  
  index_of_strong_element=random.randint(0,len(a)-1)
  strong_element=a[index_of_strong_element]
  low=list()
  mid=list()
  high=list()
  
  for elem in a:
    if elem==strong_element:
      mid.append(elem)
    elif elem<strong_element:
      low.append(elem)
    else:
      high.append(elem)
  low=quick_sort(low)
  high=quick_sort(high)
      
  result=low+mid+high

  return result


a=quick_sort(a) 
print (*a)