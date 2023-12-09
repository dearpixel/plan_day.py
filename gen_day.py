import random
import datetime

weekday = datetime.datetime.today().weekday()
themes = ("чтение","ремонт","обучение","диплом","чистка","планирование","отдых")
print("Тема: "+themes[weekday])

with open('source.txt', 'r') as file:
    for line in file:
      values = line.strip().split(" ")
      time = values[0]
      values.remove(values[0])
      random_value = random.choice(values).replace("_"," ")
      print(time+" "+random_value)
