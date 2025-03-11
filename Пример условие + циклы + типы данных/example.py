# 1) Наибольший общий делитель

first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

if first_num > second_num:
    minimum = second_num
else:
    minimum = first_num

answer = 1

for i in range(1, minimum + 1):
    if first_num % i == 0 and second_num % i == 0: # Оба числа делятся на i
        answer = i

print(answer)

# 2) Сложение и сокращение дробей

first_chisl = int(input("Числитель первой дроби: "))
first_znam = int(input("Знаменатель первой дроби"))
second_chisl = int(input("Числитель второй дроби: "))
second_znam = int(input("Знаменатель второй дроби"))

result_chisl = first_chisl * second_znam + second_chisl * first_znam
result_znam = first_znam * second_znam

minimum = min(result_znam, result_chisl) # ищет минимум из двух чисел

for i in range(1, minimum + 1):
    if result_chisl % i == 0 and result_znam % i == 0:
        result_chisl = result_chisl // i
        result_znam = result_znam // i
print(result_chisl, "/", result_znam)