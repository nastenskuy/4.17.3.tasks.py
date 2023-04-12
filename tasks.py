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
    list = whole_numbers.split()
    sum_of_integers =sum(map(int, sum_of_integers))
    return sum_list
whole_numbers ="2 -1 9 6"
sum = sum_list(whole_numbers)
print(sum)
