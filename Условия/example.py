# Важная часть языка питон - работа с условиями
# Условия помогают нам определить, какие действия надо провести с данными
#
# Пример

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

if first_number > second_number:
    print("Success", first_number) # Если условие выполнилось
elif first_number == second_number:
    print("Also success", second_number) # если не выполнилось первое условие, но необходимо проверить что-то еще
else:
    print("Not success", second_number) # если ни одно из условий не выполнилось

# Также условия можно использовать отдельно без elif и else
# Важно: если выполнилось условие из первого if, то elif проверяться не будет!!!
