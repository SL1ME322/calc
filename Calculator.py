func = int(input("Выберите функцию:\n1)Сложение\n2)Вычитание\n3)Умножение\n4)Деление\n"))
count = int(input("Введите кол-во чисел:"))
i=1
result = int(input("Введите первое число"))
for i in range(count):
    a = int(input("Введите число: ")) 
    if func == 1:
       result = result + a
    if func == 2:
       result = result - a
    if func == 3:
       result = result * a
    if func == 4:
       result = result / a
    print(result)
 

 
