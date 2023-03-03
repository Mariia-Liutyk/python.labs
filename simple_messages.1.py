import math

# Start of programming!!!
print("Task.1")
age = input("How old are you ?")
print("Nice" '\t' + age)

print("Task.2")
welcome = input("Say hello:")
print("Hello, Sasha, would you like to learn some Python today?")

print("Task.3")
# This program returns a quote
famous_person = "John Lennon"
message = input("My favorite quote press Enter:")
print('''When I was 5 years old, my mother always told me that happiness was the key to life.
When I went to school, they asked me what I wanted to be when I grew up.
I wrote down 'happy. They told me I didn't understand the assignment,
and I told them they didn't understand life.''' + famous_person )

print("Task.4")
name: str = "\n\tLiutyk \n\tMariia"
print(name)
m = name.strip()
print("of all ", m, "is my favorite")
i = name.lstrip()
print(i)
r = name.rstrip()
print(r)

print("Task.5")
print("Liutyk Mariia , Ukraine , 2356, Czarina , 157", sep='\n')

print("Task.6")
print("Конвертер величин довжини. Метри")
txt = float(input("Number>>"))
print(txt)
inches_1 = 39.37
feet_1 = 3.28
miles_1 = 0.00062137
inches = txt * inches_1
feet = txt * feet_1
miles = txt * miles_1
print("{:.2f}".format(inches))
print("{:.2f}".format(feet))
print("{:.2f}".format(miles))

print("Task.7")
holiday = float(input(' days of holiday:'))
hour = float(holiday * 24)
minute = float(holiday) * 24 * 60
seconds = float(holiday) * 24 * 60 * 60
print('{:.2f}'.format(hour))
print('{:.2f}'.format(minute))
print('{:.2f}'.format(seconds))

print("Task.8")
temperature = float(input("Enter the temperature number C:"))
f = 32 + 9/5 * temperature
k = temperature + 273.15
print('{:^15.2f}'.format(f))
print('{:^15.2f}'.format(k))

print("Task.9")
n = int(input('Press number>>'))

suma = 0

while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10

print(f'Suma: {suma}.')

print("Task 10")
x1 = 39.9075000
y1 = 116.3972300
x2 = 50.4546600
y2 = 30.5238000
n1 = math.radians(x1)
n2 = math.radians(x2)
n3 = math.radians(y1)
n4 = math.radians(y2)
distance = 6371.032 * math.acos(math.sin(n1) * math.sin(n2) + math.cos(n1) * math.cos(n2) * math.cos(n3 - n4))
print('{:>10.3f}'.format(distance))