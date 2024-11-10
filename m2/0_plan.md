# Модуль 2

## 1 Операции со строками

```python
s1 = "Панда" # в двойных кавычках
s2 = 'Panda' # или в одинарных (апострофах):
s2 = Panda # ошибка

text = '''Я Python бы выучил только за то,
что есть популярные курсы.
Много хороших курсов!''' # многострочная строка

a = ""
a = " "
s1 = "Я люблю"
s2 = "язык Python
s3 = s1 + s2
print(s3)

s3 = s1 + " " + s2
s3 = s1 + 5 # ошибка
s3 = s1 + str(5) 

"ха " * 5
"ха " * 5.5

a = "hello"
len(a)
len("") # 0
len("Python")

'ab' in "abracadabra"
'abc' in "abracadabra"

a == "hello" # ==
a == "Hello"
a != "hello"
a != "hello "

'кот' > 'кит'
'кот' > 'кот'
'Кот ' > 'кот'
ord('К')
ord('к')
```

#### Резюме

* `+` (конкатенация) – соединение строк;
* `*` (дублирование) – размножение строкового фрагмента;
* `str()` – функция для преобразования аргумента в строковое представление;
* `len()` – вычисление длины строки;
* `in` – оператор для проверки вхождения подстроки в строку;
* операторы сравнения: ==   !=   >   <
* `ord()` – определение кода символа.


### 2 Форматированный вывод

```python
x = 5.76
y = -8
print("Координаты точки: x = ", x, "; y = ", y)
print(f"Координаты точки: x = {x}; y = {y}")

age=18; name="Александр"
"Меня зовут {0}, мне {1} и я люблю язык Python.".format(name, age)
msg = "Меня зовут {0}, мне {1} и я люблю язык Python.".format(name, age)
"Меня зовут {fio}, мне {old} и я люблю язык Python. {fio}".format(fio=name, old=age)

"Меня зовут {fio}, мне {old} и я люблю язык Python. {fio}".format(old=age, fio=name)
f"Меня зовут {name}, мне {age} и я люблю язык Python."
f"Меня зовут {name.upper()}, мне {age*2} и я люблю язык Python."
f"Меня зовут {len(name)}, мне {14*2} и я люблю язык Python."
template = "%s — главное достоинство программиста. (%s)"
print(template % ("Лень", "Larry Wall"))

```


### 3 Системы счисления

```python
x = 15

print(bin(x))
print(oct(x))
print(hex(x))
```

* Кол-во бит в числе
```python
x = 16

print(bin(x))
print(x.bit_count())
print(x.bit_length())
```



```python
print(f'{10:b}') #двоичная СС
print(f'{10:o}') #8-ричная СС
print(f'{10:x}') #16-ричная СС
print(f'{10:X}') #16-ричная СС
print(f'{10:e}') # научная (экспоненциальный вид)
print(f'{10:E}') # научная (экспоненциальный вид)
print(f'{10.5:f}') # тип float (6-символов после запятой)
print(f'{100:c}') # символ юникода
```

#### Обратный перевод - функция int


> P.S 
* В математике числа обладают естественной иерархией. 
* Например, все натуральные числа являются целыми, а все целые числа — рациональными. 
* Все рациональные числа — это вещественные числа, а все вещественные числа — это комплексные числа.


### 4 Модификаторы f-строк

```python
num = 2 / 3
print(num)
print(f"{num:.3f}") # выводим число с точностью до 3-го знака
0.6666666666666666
0.667
```

### 5 Модуль math

```python
math.ceil(5.2)
math.ceil(-5.2)
math.floor(5.99)
math.floor(-3.3)
math.trunc(5.8)

math.log2(4)
math.log10(100)
math.log(2.7)
math.log(27, 3) # по основанию 3
math.sqrt(49)
math.sin(3.14/2)
math.cos(0)
math.pi
math.e
```



## 6 Побитовые операции 

```python
x = 4
y = 3
print("Побитовое или:", x | y)
print("Побитовое исключающее или:", x ^ y)
print("Побитовое и:", x & y)
print("Битовый сдвиг влево:", x << 3)
print("Битовый сдвиг вправо:", x >> 1)
print("Инверсия битов:", ~x)
```

##  [7 Практика строки](module-1\4_string.md)

## 8 Логический тип bool. Операторы сравнения `>=, !=, <=, ==и` операторы `and, or, not`

```python
4 > 2
4 > 7
a = 5
b = 7.8
a <= b
res = a > b
type(res)
x % 2 == 0
x % 2 != 0
a % 3 == 0

print (1 or 3) #?
print (1 and 3) #?
x % 2 == 0 or x % 3 == 0


bool(1)
bool(-10)
```


## Условный оператор if. Конструкция if-else

### 1 Тернарный оператор

```python
a = float(input("a: "))
b = float(input("b: "))
# Если a меньше b:
if a < b:
    a, b = b, a
print(a, b)

res = a if a > b else b
res = abs(a) if a > b else abs(b)
```

### 2 Составные условия

```python
x = int(input())
if x >= -4 and x <= 10:
    print("x в диапазоне [-4; 10]")

# if -4 <= x <= 10
```

### 3. Вложенные условия и множественный выбор. Конструкция if-elif-else

```python
x = int(input())
if x % 2 == 0:
    if 0 <= x <= 9:
        print("x - четная цифра")
    else:
        print("x - четное число")
```

```
1. Курс по Python
2. Курс по С++
3. Курс по Java
4. Курс по JavaScript
```


```python
item = int(input())
 
if item == 1:
    print("Выбран курс по Python")
else:
    if item == 2:
        print("Выбран курс по C++")
    else:
        if item == 3:
            print("Выбран курс по Java")
        else:
            if item == 4:
                print("Выбран курс по JavaScript")
            else:
                print("Неверный пункт")

```

## [3 Практика if-elif-else](/module-2/1_if-else-elif.md)


## Pattern matching. Конструкция match


* пример 1

```python
language = "english"
language = "russian"

match language:
    case "russian":
        print("Привет")
    case "english":
        print("Hello")
    case "german":
        print("Hallo")

    case _:
    print("Undefined")

```

* пример 2

```python
case "american english" | "british english" | "english":
    print("Hello")

```


* пример 3

```python
day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Work")

```


* пример 4

```python
cmd = 10
 
match cmd:
    case str() as command:
        print(f"строковая команда: {command}")
    case int() as command:
        print(f"целочисленная команда: {command}")
    case bool() as command:
        print(f"булева команда: {command}")
    case _:  # wildcard
        print(f"другая команда")


сmd = "c_top"
 
match cmd:
    case str() as command if len(command) < 10 and command[0] == 'c':
        print(f"строковая команда: {command}")
    case bool() as command:
        print(f"булева команда: {command}")
    case int() as command if 0 <= command <= 9:
        print(f"целочисленная команда: {command}")
    case _:  # wildcard
        print(f"другая команда")


```


##  [4 Практика match](module-2/2_matching.md)

##  [Домашка](module-2/3_homework.md)