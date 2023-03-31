import pyodbc as odbc
import os
import smtplib, ssl
from random import randint
from datetime import datetime






#import pyodbc as odbc
#import os
#import smtplib, ssl
#from random import randint
#from datetime import datetime
#
#DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
#SERVER_NAME = 'DESKTOP-LR7RPC4\DAMIR'
#DATABASE_NAME = 'FoodPython'
#NAME = 'DESKTOP-LR7RPC4\Honor'
#class Connection:
#    def __init__(self) -> None:
#        self.conn = odbc.connect('DRIVER='+DRIVER_NAME+';SERVER='+SERVER_NAME+';DATABASE='+DATABASE_NAME +';SERVER='+SERVER_NAME+';Trusted_Connection=yes')
#        pass 
#
#    def select(self, sql) -> list:
#        cursor = self.conn.cursor()
#        cursor.execute(sql)
#        list = []
#        for row in cursor:
#            list += (row, )
#class User:
#     def __init__(self) -> None:
#         
#         pass
 









DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'DESKTOP-LR7RPC4\DAMIR'
DATABASE_NAME = 'FoodPython'
NAME = 'DESKTOP-LR7RPC4\Honor'
conn = odbc.connect('DRIVER='+DRIVER_NAME+';SERVER='+SERVER_NAME+';DATABASE='+DATABASE_NAME +';SERVER='+SERVER_NAME+';Trusted_Connection=yes')
cursor = conn.cursor()
print(conn)
 
conn.commit()


 
def CockroachAdd(amount, price, userID):
   
    print(userID)
    random = randint(1,6)
    playerRandom = randint(1,6)
    sale = 0
    loyalty_card = 0
    if (price >= 5000):
        cursor.execute(f"insert into [dbo].[Order]([Amount],[Price] ,[Sale],[Loyalty_Card], [Date],[User_ID]) values ('{amount}','{price}','{sale}','{loyalty_card}','{dt_string}','{userID}')")
    conn.commit()
    if (price >= 15000):
        loyalty_card = price * 10/100 
    if (price >= 20000):
        loyalty_card = price * 20/100
    if (random == playerRandom):
        print("Просим прощения, но в вашем блюде был найден таракан( В честь этого стоимость на блюда будет снижена на 30%")
        sale = price * 30/100
        print("Теперь цена заказа: ", price)
    
         
    price = (price * amount) - sale - loyalty_card
    print("Скидка по карте:",loyalty_card)
    print(f"Количество: {amount}\nЦена заказа: {price}")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     
     

    cursor.execute(f"insert into [dbo].[Order]([Amount],[Price] ,[Sale],[Loyalty_Card], [Date],[User_ID]) values ('{amount}','{price}','{sale}','{loyalty_card}','{dt_string}','{userID}')")
    conn.commit()
    print (dt_string)
    return price

def Registration():
    AdminCode = 'ZXC3221488'
     
    print("Регистрация\nВыберить роль регистрации:\n1.Пользователь\n2.Администратор\n3.Выйти")
    choise = int(input())
    if (choise == 1):
        Role = 'user'
        print("Введите логин:")
        Login = input()
        print("Введите пароль:")
        Password = input()
        print("Введите адрес электронной почты:")
        Email = input()
        cursor.execute(f"insert into [dbo].[User]([User_Role],[Login],[Password],[Email],[Balance]) values('{Role}','{Login}','{Password}','{Email}','5000')")
        conn.commit()
        print("Вы успешно зарегистрировались")
    if (choise == 2):
        Role = 'admin'
        print("Введите логин:")
        newLogin = input()
        print("Введите пароль:")
        newPassword = input()
        print("Введите адрес электронной почты:")
        newEmail = input()
        print("Введите верификационный код, выданный организацией:")
        code = input()
        if code!=AdminCode:
            print('Ошибка! Вы ввели неверный код. Повторите попытку регистрации.')
            Registration()
        else:
            cursor.execute(f"insert into [dbo].[User]([User_Role],[Login],[Password],[Email],[Balance]) values('{Role}','{newLogin}','{newPassword}','{newEmail}','{5000}')")
            conn.commit()
            print("Вы успешно зарегистрировались")
 
 
def Authorization():
    os.system('cls')
    
    print("Авторизация\nВыберить роль авторизации:\n1.Пользователь\n2.Администратор\n3.Выйти\n") 
    choise = int(input())
    if (choise == 1):
        SelectRole('user')
    if (choise == 2):
        SelectRole('admin')
    if (choise == 3):
        quit 
    else:
      
        input("Нажмите Enter, чтобы продолжить...")
        Authorization()
     
    #проверку
    

    
def SelectRole (Role):
    print("Введите логин:")
    Login = input()
    print("Введите пароль:")
    Password = input()    
    cursor.execute(f"SELECT *  FROM [dbo].[User] where [Login] = '{Login}' AND [Password] = '{Password}' AND [User_Role] = '{Role}'")
    
    results =  cursor.fetchone()
    userId =  results[0]
    rowCount = len(results) 
    print(results)
    
    if rowCount == 0: 
        print("Ошибка! Неверный логин/пароль")
    else:
        os.system('cls')
        if (Role == 'user'):
            Order(userId)
            
        if (Role == 'admin'):
            AdminWindow()

def Order(userId):
     print("Вы авторизовались в систему!")
     os.system('cls')
     print("Добро пожаловать!\nБлюдо: Котлета по-киевски\nЦена за штуку - 200 рублей.\nАКЦИЯ:При покупке 3 котлет - 4-я в подарок") 
     print("Покупка: \nВ блюде должны присутствовать горох и зелень для закуски ?\n1)Да\n2)Нет\n")
     choise =  input()
     price =  cursor.execute (f"select SUM(Price) from [dbo].[Ingredients]")
     result = cursor.fetchone()
     price = result[0]
     if (choise == "1"):
        price +=20
        print("Горох и зелень добавлены в блюда")
     else: "Ошибка. Введите 1 или 2"
     print("Выберите кол-во котлет:")
     amount = int(input())
     #доп блюда
     additional = 0
     #range для int
     for i in range(amount):
        if (i//4):
            additional +=1
     if(additional != 0):
        print (f"По акции вам было добавлено еще {additional} блюд/о")
     CockroachAdd(amount, price, userId)
     cursor.commit()
     
def AdminWindow():
    os.system('cls')
    cursor.execute (f"select SUM(Price) from [dbo].[Ingredients]")
    result = cursor.fetchone()
    number = [x for x in result]
    
    cursor.commit()
    print(result)
    print("Добро пожаловать в меню администратора!\nФункции:\n1.Поменять цену ингредиентов\n2)Изменить полностью ингредиент/ы\n3.Назад к авторизации")
    cursor.execute ("Select * from [dbo].[Ingredients]")
    result = cursor.fetchall()
    print ("Ингредиенты: ")
    print(result)
    ingredientAct = int(input()) 
    if (ingredientAct == 1):
        print("Введите номер ингредиента для изменения цены:")
        ID = int(input())
        print("Введите измененную цену ингредиента:")
        Price = int(input())
        cursor.execute (f"exec Ingredients_update {ID}, '{Price}'")
        cursor.commit()
        print('Цена ингредиента изменена!')
        input("Нажмите Enter, чтобы продолжить...")
        AdminWindow()
    if (ingredientAct == 2):
        print("Введите номер ингредиента для изменения цены:")
        ID = int(input())
        print("Введите новое название ингредиента:")
        Name =  input() 
        print("Введите новую цену ингредиента:")
        Price = int(input())
        print("Введите новое количество ингредиента:")
        Stock = int(input())
        cursor.execute (f"exec Ingredients_Full_Update {ID}, '{Name}','{Price}','{Stock}'")
        cursor.commit()
        print('Ингредиент изменен!')
        input("Нажмите Enter, чтобы продолжить...")
        AdminWindow()
    if (ingredientAct == 3):
        Authorization()
 
Authorization()

 

