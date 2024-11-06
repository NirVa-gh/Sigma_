"""def coffe(temp,value,timer = 15,mode = "Default"):
    print(f"нагревание воды до {temp}")
    print(f"готовка кофе {timer} секунд")
    print(f"подготовка {value} количества")
    print(f"готовка в режиме {mode}")

coffe(100,15,"1l","Manual") #позиционные аргументы
coffe(50,"90","0.5l","Auto")

coffe(value=14,temp=15) #именованные аргументы
def make_shirt(size, text):
    print(f"футболка размером {size} и тестом {text}")

make_shirt("45","test")
make_shirt(test="kykyk",size=50)"""

def get_sum(a=0,b=0):
    print(a+b)

def get_devide(a=1,b=1): #get_devide=a/b
    return a/b


get_sum(5,9)
a=get_devide(10,2)
print(a)


def build_person(first_name, last_name):  #build_person = person
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)