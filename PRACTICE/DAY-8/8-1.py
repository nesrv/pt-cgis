class Lamp:
    brand = 'Эра'
    count = 0

    def __init__(self, floor=0):
        self.state = False
        self.floor = floor
        Lamp.count +=1
        self.count = Lamp.count
        print('создана лампочка №', Lamp.count)

    def switch_on(self):
        if self.state == False:
            self.state = True
            print('лампочку включили')

    def switch_off(self):
        if self.state == True:
            print('лампочку выключили')
            self.state = False

    def __str__(self):
        return f'Я лампочка № {self.count} "{Lamp.brand}" на {self.floor} этаже'

lamp1 = Lamp(10)
lamp2 = Lamp(5)

lamp1.switch_on()

lamp1.switch_off()

print(lamp1.floor)

print(lamp1)
print(lamp2)
