'''test,a = float(input("Enter test -")), float(input("Enter a -"))
print(type(test))
list = [1,2,3,4]

for i in list:
        list[i] = input("")
print(list)'''

'''while True:
        city = input("promt")
        if city == 'quit':
                break
        else:
                print("I'd love to go to " + city.title() + "!")'''

current_number = 0
while current_number < 10:
        if current_number % 2 == 0:
                continue
        print(current_number)

list = ["test","first"]
list.remove("test")
list.pop(2)
del list[1]
