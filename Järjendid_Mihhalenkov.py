#Самостаятельная работа.
список_покупок = []
предмет = input("Что ты хочешь добавить в список покупок? ")
список_покупок.append(предмет)
print(список_покупок)
while True:
    значение = input("Что ты хочешь добавить в список покупок? Чтобы завершить список введи 'q': ")
    if значение == 'q':
        break
    else:
        список_покупок.append(значение)
print(список_покупок)
for предмет in список_покупок:
    if предмет == "piim":
        print("Hind piim: 1.25€")
    elif предмет == "leib":
        print("Hind leib: 0.75€")
    elif предмет.isdigit():
        print(f"{предмет} это число.")
    elif предмет.isalpha():
        print(f"{предмет} это предложение написано буквами.")
    elif предмет.isalnum():
        print(f"{предмет} это состоит из цирф или букв.")
    elif предмет.islower():
        print(f"{предмет} это все написано маленькими буквами.")
    elif предмет.isupper():
        print(f"{предмет} это все написано большими бувами.")
    elif предмет.istitle():
        print(f"{предмет} начинается с заглавной буквы.")
    else:
        print(f"{предмет} Написано капсом: {предмет.upper()}")
        print(f"{предмет} Без капса: {предмет.lower()}")
        print(f"{предмет} Первая буква заглавная: {предмет.capitalize()}")
print()
print()
print()
spisok=[] #Пустой список.
numbers=[1,2,3,4,5]
abc=['A','B','C']
slovo="Programmerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить букву на i -позицию")
    print("4-удалить элемент")
    valik=int(input())
    if valik==1:
        a=input("Введи букву: ")
        slovo_list.append(a)
        print(f"Добавили {a} новый список",slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить: ")
        i=input("Введи номер позиции, куда хочешь добавить букву: ")
        slovo.list.insert(i-1,a) #0,1,2...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить: ")
        n=slovo_list.count(a)
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(slovo_list)
