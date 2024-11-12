# Циклы
import time

x = 5

while x > 1:
    print('работаю ...', x)
    time.sleep(1)
    x = x - 1
    if x == 0:
        break
else:
    print('happy end')


print("конец цикла")

