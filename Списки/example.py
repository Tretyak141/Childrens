# Также в питоне реализовано хранение данных в списке
#
# Список - коробочка, в которой могут лежать разные данные

animals_list = ["cat", "dog", "horse", "elephant", "fish"]

# Пройти по списку циклом

for animal in animals_list:
    print(animal)

# Добавить в список
animals_list.append("Snake")

# Удалить из списка

animals_list.remove("cat")
animals_list.pop(2) # Удаление по порядковому номеру в списке, нумерация с нуля!!!!!

# Сумма элементов списка
summa = sum(animals_list)

# Длина списка
list_length = len(animals_list)

# Также существует функция, оставляющая только уникальные значения в списке

unique_animals = set(animals_list)

# Есть возможность взять "срез" списка - элементы от и до

new_list = animals_list[2:5]