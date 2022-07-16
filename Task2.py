#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def multyply (list:list):
    result = []
    j = len(list)//2 +len(list)%2
    print (j)
    for i in range (j):
        result.append (list[i]*list[-1-i])
    return result

list1 = [2, 3, 4, 5, 6]
list11 = multyply(list1)
list2 =[2, 3, 5, 6]
list22 = multyply(list2)
print (f"{list1} -> {list11}")
print (f"{list2} -> {list22}")