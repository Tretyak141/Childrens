# Если одни и те же вычисления происходят в коде на постоянной основе,
# их удобнее обернуть в функцию

def socratit_drob(chisl, znam):
    new_chisl = chisl
    new_znam = znam
    minimal = min(chisl, znam)
    for i in range(1, minimal + 1):
        if new_chisl % i == 0 and new_znam % i == 0:
            new_chisl = new_chisl // i
            new_znam = new_znam // i
    return new_chisl, new_znam

a = 15
b = 5
a, b = socratit_drob(a, b)

#Отмечу, что после строчки, в которой написано return, код не выполняется

def func_example(parameter):
    # Функция вернет True если параметр parameter равен 10, иначе вернет False
    if parameter == 10:
        return True
    return False