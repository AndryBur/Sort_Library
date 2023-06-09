a=[6,5,3,4,8,7,7]
print(*a)                             

def merge(al, ar): 
  sorted_a=list()
  current_left=0
  current_right=0

  lenl=len(al)
  lenr=len(ar)

  for i in range(lenl+lenr):
    if current_left<lenl and current_right<lenr:
      if al[current_left]>ar[current_right]:
        sorted_a.append(al[current_left])
        current_left+=1
      else:
        sorted_a.append(ar[current_right])
        current_right+=1
    else:
      if current_left==lenl:
        for j in range(current_right, lenr):
          sorted_a.append(ar[j])
      else:
        for j in range(current_left, lenl):
          sorted_a.append(al[j])
      break
  return sorted_a

def merge_sort(a):
  if len(a)<=1:
    return a
  mid=len(a)//2
  left_side=a[:mid]
  right_side=a[mid:]
  
  left_side=merge_sort(left_side)
  right_side=merge_sort(right_side)

  result=merge(left_side, right_side)
  return result


a=merge_sort(a) 
print (*a)