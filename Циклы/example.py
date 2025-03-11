# Для выполнения нескольких однотипных действий подряд
# в питоне используются циклы

# Всего в питоне три вида циклов

# 1) Цикл с условием

a = 10
while (a < 40):
    a = a + 1

# 2) Цикл по какому-либо списку

animals = ["cat", "dog", "cat", "horse"]

counter_cat = 0
counter_dog = 0
counter_horse = 0

for animal in animals:
    if animal == "cat":
        counter_cat = counter_cat + 1
    elif animal == "dog":
        counter_dog = counter_dog + 1
    else:
        counter_horse = counter_horse + 1

# 3) Цикл по числам подряд
и
for i in range(1,20): # на каждом витке цикла i принимает значение от 1 до 20
                    # (последнее число не включительно, особенность языка)
    print(i)