result = 0
year = int(input("Введите год: "))
#Январь
for i in range (1, 31):
    result+= i
#Февраль
if(year%4 ==0):
    for i in range (1, 29):
        result+= i
else:
    for i in range (1, 28):
        result+= i
#Март
for i in range (1, 31):
    result+= i
#Апрель
for i in range (1, 30):
    result+= i
#Май
for i in range (1, 31):
    result+= i
#Июнь
for i in range (1, 30):
    result+= i
#Июль
for i in range (1, 31):
    result+= i
#Август
for i in range (1, 31):
    result+= i
#Сентябрь
for i in range (1, 30):
    result+= i
#Октябрь
for i in range (1, 31):
    result+= i
#Ноябрь
for i in range (1, 30):
    result+= i
#Декабрь
for i in range (1, 31):
    result+= i
print("Результат: ",result)