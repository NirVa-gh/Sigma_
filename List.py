list_1 = ["Matvey","Ilya","Miron","Darya"]
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
print(a)








