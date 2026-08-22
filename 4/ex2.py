student = ("Ali", 20, 18.5)

print(f"name is = {student[0]} age is {student[1]} and avg is = {student[2]}")

student[1] = 21

# TypeError: 'tuple' object does not support item assignmen
# این ارور رخ میدهد بدلیل اینکه نمی توان به تاپل ایتم اضافه یا حذف کرد و یا مقادیر انها را تغیر داد زیرا تاپل 
#imutable 
#می باشد
