#------------------Списки------------------------------
"""list_1 = ["Matvey","Ilya","Miron","Darya"]
list_2 = ["Leonid","Fedor","Makar","Leonid"]

list_1.append("test") #Добавление в список
print(f"#Добавление в список {list_1}")
list_1.remove("test") #Удаление объекта из списка
print(f"#Удаление объекта из списка {list_1}")
del list_2[2] # Удаление, но для всех
print(f"#Удаление, но для всех {list_2}")
list_1.insert(1,"insert") # Добавление объекта в определенный индекс
print(f"Добавление объекта в определенный индекс{list_1},{list[2]}")
a = list_2.pop(2)
print(a)"""
#------------------Условный оператор----------------------------

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':  #если car равно bmw то
        print(car.upper()) # Выполняется в if блоке
        print(car.upper()) # Выполняется в if блоке
    else:              #иначе
        print(car.title()) # будет работать для esle блока
    print(car.title()) # Будет работать для for блока
print(car.title())  # Будет работать для основной программы

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
else:
    print("That is correct answer")

alien_color = "green"
if alien_color == "green":
    print("u got a 5$")
