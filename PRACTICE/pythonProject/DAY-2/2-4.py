# метод format и f-строки

name = 'Егор'
first_name = 'Петров'

s = 'Имя: {first_name} Фамилия: {name}'.format(name=name, first_name=first_name)

print(1, s)

# f-строки

s = f'Имя: {name + " Васильевич"} Фамилия: {first_name.upper()}'
print(2, s)
print(f'{32:b}')
print(f'{15:X}')
print(f'{1.23456:.10%}')