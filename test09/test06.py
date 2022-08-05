# file: test06.py

class Car:
    kind = 'Sedan'
    countOfDoors = 5

    def __init__(self, name1):
        self.name = name1

    def sethorsepower(self, power):
        self.horsepower = power

    def driving(self, city):
        print('%s로 운전중입니다.' % (city))

class Chacha(Car):
    autoPilot = True
    countOfAirbag = 10

    def setWheelSize(self, wheel):
        self.wheelSize = wheel

    def driving(self, city):
        print('%s(으)로 자동 운전중 입니다.' % (city))

    def turnning(self, power):
        self.turnninghorsepower = self.horsepower + power
        return self.turnninghorsepower



toch = Car('touch')
toch.horsepower = 120
toch.driving('서울')

print('마력 : ', toch.horsepower)
print()

cha = Chacha('좋은차')
cha.sethorsepower(300)
cha.setWheelSize(20)
cha.turnning(200)
cha.driving('밀라노')
print('차이름 : ', cha.name)
print('마력 : ', cha.horsepower)
print('바퀴 크기 : ', cha.wheelSize)