# Завдання №1
# Звичайний список без функцій:
all_countries = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian', 'Ireland','USA']
print(all_countries)
print(sorted(all_countries))# сортує список за алфавітом
all_countries.reverse()
print(all_countries)# зворотній порядок списку
all_countries.sort(reverse=True)
print(all_countries)# сортує у спадному порядку
# Завданя №2
def sum_list(whole_numbers):
    sum_of_integers = whole_numbers.split()
    sum_list = sum(map(int, sum_of_integers))
    return sum_list
whole_numbers ="3 -4 -5 12"
sum = sum_list(whole_numbers)
print(sum)
# Завдання №3
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities.insert(5, "and")
print(cities)
# Завдання №4
line = "7 8 9"
list = line.split(" ")
print(list)
line2 = sorted(list, reverse = True)
l = int(''.join(map(str,line2)))
print(l)
# Завдання №5
my_friends =["Maria","julia","Olga","Bogdana","Mykola","Dmytro","Peter","Vanya"]
print(','.join(my_friends))#Перетворює список у рядок
print(len(my_friends))#Повертає к-ть елементів списку
print(my_friends.index("Olga"))#Знаходить індекс елемента у списку
print(my_friends.append("Lola"))#Додає елементи в кінець списку
print(my_friends.insert(5,"Lola"))#Додає елемент на конкретну позицію
print(my_friends.pop())#Видаляє елемент зі списку і водночас отримує його зі списку
