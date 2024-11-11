

__Задача 1__ Даны длины сторон треугольника. Вычислите его периметр и площадь.

#### Формат входных данных

На вход программе даются три целых числа, длины сторон треугольника.
Гарантируется, что треугольник с заданными сторонами существует.

##### Формат выходных данных

Требуется вывести два числа — __периметр__ и __площадь__ треугольника с заданными сторонами.

##### Решение задачи

```python
# TODO: you code here...
```

---

### Данные для самопроверки
|   a   |   b   |   c   |   |   S    |   P   |
| :---: | :---: | :---: |---|  :---: | :---: |
|   3   |   4   |   5   |   |    6   |   12  |
|   6   |   5   |   5   |   |   12   |   16  |
|   15  |   13  |   4   |   |   24   |   32  |
### Подсказки

<details>
<summary>Подсказка-1</summary>
Для расчета площади треугольника воспользуйтесь "формулой Герона"
</details>



__Задача 2.__  Дано трехзначное число. Найдите его первую и последнюю цифру.
Примечание: решите задачу без преобразования числа к строке

#### Формат входных данных
Дано целое положительное трехзначное число.
#### Формат выходных данных
Требуется вывести первую и последнюю цифру числа

```python
number = int(input("Введите трехзначное число: "))
first = ...
last = ...
print("Первая цифра числа =", first)
print("Последняя цифра числа =", last)
```
### Данные для самопроверки
|  number  | |   first   |  last    |
| :---: | ---| :---: | :---: |
|   143   | |   1  |   3  |
|   894   | |   8  |   4  |
|   666  |  |   6  |   6  |
|   240  |  |   2  |   0  |

### Подсказки

<details>
<summary>Подсказка-1</summary>
Воспользуйтесь операцией %(остаток от деления) и //(целочисленное деление)
</details>

<details>
<summary>Подсказка-2</summary>
Посмотрите результаты выражений(например, в <i>python-shell</i>): <br>
<b>12 % 10</b> <br>
<b>45 % 10</b> <br>
<b>237 % 10</b> <br>
<b>237 % 100</b> <br>
</details>

<details>
<summary>Подсказка-3</summary>
Посмотрите результаты выражений(например, в <i>python-shell</i>): <br>
<b>69 // 10</b> <br>
<b>1234 // 10</b> <br>
<b>1234 // 100</b> <br>
<b>1234 // 1000</b> <br>
</details>



__Задача 3.__

Существует бесконечно высокий дом, в котором нумерация квартир начинается с единицы. 

Известен номер квартиры. 

Определите на каком этаже находится данная квартира, если всего на этаже располагается по 5 квартир.

### Формат входных данных

Дано целое положительное число - номер квартиры

### Формат выходных данных

Вывести целое число - номер этажа, на котором расположена заданная квартира

__Примечание__: постарайтесь решить задачу без использования оператора if

#### Решение задачи

```python
# TODO: you code here...
```

---

### Данные для самопроверки
|   flat   | | floor    |
| :---: |---| :---: |
|   1   |   |   1   |
|   2   |   |   1   |
|   5   |   |   1   |
|   7   |   |   2   |
|   9   |   |   2   |
|   10   |  |   2   |
|   12   |  |   3   |
|   45   |  |   9   |
|   46   |  |   10   |
### Подсказки

<details>
<summary>Подсказка-1</summary>
Нарисуйте схему дома, пропишите квартиры на первых пяти этажах. <br>
Попробуйте найти закономерность(формулу) между номером квартиры и этажом.
</details>

<details>
<summary>Подсказка-1</summary>
Уверяю вас, задача решается теми инструментами, что мы изучили. <br>
Но! Не стесняйтесь гуглить. Если вам нужен какой-то дополнительный инструмент питона, а вы его не знаете - найдите.
</details>


__Задача 4.__  Вводятся координаты точки А - x и y. Найти расстояние от точки А до начала координат

## Входные данные:

> 3 4

## Выходные данные:

> 5

__Задача 5.__  Вводятся координаты двух точек А(x,y) и B(x1,y1). Найти расстояние между точками

## Входные данные:

> 1 1
> 4 5

## Выходные данные:

> 5


## Логические операции


__Задание 6.__ Вводится вещественное число. Нужно определить, что его целая часть кратна 3.

На экран вывести `True`, если кратно и `False` - в противном случае. 

Задача делается без использования условного оператора.

## Входные данные:

> 78.34

## Выходные данные:

True

__Задача 7.__ Вводится стоимость книги X рублей (например, X = 435.78) - положительное вещественное число с точностью до сотых (два знака после запятой).
Требуется определить, является ли дробное значение (число после запятой) больше 50.
На экран вывести True, если больше и False - в противном случае. Задача делается без использования условного оператора.

## Входные данные:

> 456.56

## Выходные данные:

> True

__Задача 8.__ Вводятся два целочисленных значения в одну строчку через пробел. Можно прочитать с помощью команды:

```python
a, b = input().split()
```


Необходимо определить, можно ли первое число нацело разделить на второе. На экран вывести True, если делится и False - в противном случае. Задача делается без использования условного оператора.

## Входные данные:

> 12 3

## Выходные данные:

> True

__Задача 9.__ Вводятся три целых положительных числа.

Необходимо определить, можно ли их интерпретировать (воспринимать) как длины сторон треугольника. (Сумма длин двух произвольных сторон всегда должна быть больше третьей стороны). На экран вывести `True`, если треугольник формируется и `False` - в противном случае. 

Задача делается без использования условного оператора.

## Входные данные:

> 8 11 12

## Выходные данные:

> True

__Задача 10.__ Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон `[0; 2]` или в диапазон `[10; 20]` (включительно). На экран вывести `True`, если попадает и `False` - в противном случае. 

Задача делается без использования условного оператора.

## Входные данные:

> 1.2

## Выходные данные:

> True
