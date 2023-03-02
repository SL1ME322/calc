result = 0
year = int(input('Введите год: '))
mult = 1
#Январь
for i in range (1, 32):
    if (i>9):
            d1 = i % 10
            d2 = i % 100 // 10
            result+= d1 + d2
           
    if(i<10):
           
             result+=i
 
#Февраль
if(year%4 ==0 and year%100!=0 or year%400 == 0):
     
    for i in range (1, 30):
         
        if (i>9):
            d1 = i % 10
            d2 = i % 100 // 10
            result+= d1 + d2
        if(i<10):
             result+=i
else:
    for i in range (1, 29):
         if (i>9):
            d1 = i % 10
            d2 = i % 100 // 10
            result+= d1 + d2
         if(i<10):
            result+=i
#Март
for i in range (1, 32):
     if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
     if(i<10):
             result+=i
#Апрель
for i in range (1, 31):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Май
for i in range (1, 32):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Июнь
for i in range (1, 31):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Июль
for i in range (1, 32):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Август

for i in range (1, 32):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Сентябрь
for i in range (1, 31):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Октябрь
for i in range (1, 32):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Ноябрь
for i in range (1, 31):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
             result+=i
#Декабрь
for i in range (1, 32):
    if (i>9):
            d1 = i % 10
             
            d2 = i % 100 // 10
            result+= d1 + d2
    if(i<10):
            result+=i
print('Результат:', result)
 

 
