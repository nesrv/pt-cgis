# Ветвления. Тернарный оператор


__Задание 1.  Времена года__
Пользователь вводит номер месяца (целое число). 

1 - это январь, 

2 - это февраль и так далее.

Программа пишет, какой это сезон (зима, весна, лето или осень). Если номер месяца неправильный (например, 13), программа сообщает что что-то неправильно ввели.


__Задание 2.  Существует ли треугольник__


По длинам трех отрезков, определить возможность существования треугольника, составленного из этих отрезков. Определите тип треугольника

### Формат входных данных

Даны три целые положительные числа, длины сторон треугольника.

### Формат выходных данных

Вывести "Существует", если можно построить треугольник с заданными длинами сторон, и "Не существует", если невозможно.
Далее через запятую выводится тип треугольника

### Решение задачи

```python
# TODO: you code here...
```

---

### Данные для самопроверки

| a | b | c | Результат |
| :---: | :---: | :---: | --- |
|   3   |   4   |   6   | Существует   |
|   3   |   4   |   5   | Существует, прямоугольный   |
|   2   |   4   |   19   | Не существует |
|   6   |   6   |   6   | Существует, равносторонний |
|   4   |   4   |   8   | Не существует |
|   1   |   1   | $$  \sqrt2 $$  | Существует, равнобедренный и прямоугольный |
### Подсказки

<details>
<summary>Подсказка-1</summary>
Треугольник существует только тогда, когда сумма длин любых его двух сторон больше третьей стороны.
</details>

__Задание 3.  Светофор__

Работа светофора для пешеходов запрограммирована следующим образом: в начале каждого часа в течение трех минут горит зеленый сигнал, затем в течение двух минут – красный, в течение трех минут – опять зеленый и т. д.

Дано вещественное число t, означающее время в минутах, прошедшее с начала очередного часа. Определить, сигнал какого цвета горит для пешеходов в этот момент. На экран вывести сообщение (без кавычек) "green" - для зеленого и "red" - для красного.
## Входные данные:
12.5
## Выходные данные:
green


