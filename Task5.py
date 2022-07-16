#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def createList(list,k):
    if k <=2 : return list
    for i in range(k-2):
        
        list.append(list[-1]+list[-2])
        list.insert(0,list[1]-list[0])
    list.append(list[-1]+list[-2]) #чтобы было как в указанном примере
    return list



initList = [-1,1,0,1]
k = 8
fiboList = createList(initList,k)
print (fiboList)

