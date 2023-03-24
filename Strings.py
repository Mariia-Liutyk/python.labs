print("Task 1")
names = ["Maks", "Olena", "Katya"]
for i in range(len(names)):
    print(names[i])

print("Task 2")
transport = ["bike", "bicycle", "train"]
print("Я хотів би купити" '\t' + transport[1])

print("task 3")
years_list = [2005, 2006, 2007, 2008, 2009, 2010]
print("Мені виполнилося 3 роки" '\t' + str(years_list[2]))
years_list.append(2011)
print(years_list)
print("Мені найбільше було років в " '\t' + str(years_list[5]) + '\t' "році")

print("Task 4")
things = ['wallet', 'mirror', 'umbrella']
s = things[2].capitalize()
print(s)
print(things)
t = things[2].upper()
print(t)
print(things)
del things[2]
print(things)

print("Task 5")
languages = ['Georgian', 'Estonian', 'Ukrainian']
p = languages[-1].lower()
print(p)
languages_is = p[::-1].capitalize()
print(languages_is)

print("Task 6")
hardware = ("orange", "lemon", "peach")
(A, B, C) = hardware
print(A)
print(B)
print(C)

a = list(hardware)
a[1] = "kiwi"
hardware = tuple(a)
print(hardware)

software = ["apple", "banana", "cherry"]
for i in range(len(software)):
    print(software[i])
software[1] = "blackcurrant"
print(software)

# задачі
print("task 2.1")
names_lang = ['Ukrainian', 'French', 'Bulgarian', 'Norwegian', 'Latvian']
names_lang.reverse()
print(names_lang)
names_lang.sort(reverse=True)
print(names_lang)
w = sorted(names_lang, reverse=True)
print(w)

print("task 2.2")
numbers = input().split()
sum = 0
for num in numbers:
    sum += int(num)
print(sum)

print("task 2.3")
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
message = ', '.join(cities[:-1]) + ' and ' + cities[-1]
print(message)

print("task 2.4")
input_str = input("Введіть 5 цифр, розділених пропусками: ")
num_list = input_str.split()
num_list = [int(num) for num in num_list]
reverse_num_list = num_list.copy()
reverse_num_list.sort(reverse=True)
reverse_num_str = ''.join([str(num) for num in reverse_num_list])
reverse_num = int(reverse_num_str)
print("Число, утворене зі зворотньо впорядкованого списку: ", reverse_num)

print("task 2.5")
inform_color = ['Black', 'Brown', 'Violet', 'Gold']
print(len(inform_color))
print(type(inform_color))
if 'Gold' in inform_color:
    print("Yes, 'Gold' is in my list 'inform_color'")
new_l = inform_color.insert(2, 'Red')
print(new_l)
inform_color.append('Pearl')
print(inform_color)
for i in inform_color:
    print(i)
new_l2 = [x.upper() for x in inform_color]
print(new_l2)
inform_color.sort()
print(inform_color)
inform_color.reverse()
print(inform_color)
m = inform_color.copy()
print(m)
m2 = list(inform_color)
print(m2)
inform_color.count('Black')
print(inform_color)
tuple(inform_color)
print(inform_color)
