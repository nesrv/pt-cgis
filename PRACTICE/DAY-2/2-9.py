# Циклы
x = 1
# Моржовый оператор := (моржик)


while (passw := input("введи пароль - >")) != '123':
    print(f'Пароль {passw} неправильный. Попытка № {x}')
    if x == 3:
        print('Доступ запрещен. Попытки закончились')
        break
    x += 1
else:
    print('Доступ разрешен')

