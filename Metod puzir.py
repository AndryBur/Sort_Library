a=[8,7,6,5,4,2,1,3]
is_sorted=True                       # Вопрос 2. Установим флаг сортировки. Изначально он равен True
print(*a)                             

for i in range(len(a)):
    for j in range((len(a)-1)-i):    # Вопрос 1. В виду того, что мы после каждого прохода неотсортированных значений становится на 1 меньше (этим мы уменьшаем длину сортировки 
                                     # и таким образом ускоряем процесс)
        if a[j]<a[j+1]:
            is_sorted=False          # Вопрос 2. В процессе выполнения условия сравнения значений элементов во втором цикле, флаг сортировки определим как False. 
                                     # Самим переназначением переменной мы утвердили что условие выпонено и будет замещение элементов
            a[j],a[j+1]=a[j+1],a[j]
                                 
    if is_sorted==True:            # Вопрос 2. После выполнения второго цикла замещения проверим значение флага сортировки. Если значение осталось True, значит условие для 
           break                     # замещения не сработало и все элементы отсортированы и мы останавливаем работу основного цикла, а соответственно кода сортировки.
    else:
        is_sorted=True               # Вопрос 2. Если значение флага поменялось на False, значит произошла замена. Вследствии чего мы возвращаем значение флага опять True и 
                                     # продолжаем основной цикл в сортировке. Этим методом мы прекращаем нулевые операции и сокращаем время процесса сортировки.                 
    
    print(a)       

print (*a)