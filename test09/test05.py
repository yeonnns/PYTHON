# file: test05.py

# 18인치의 바퀴를가진 2,000cc의 빨간차는 전진, 후진, 우회전, 좌회전 기능이 있다.

class Car:
    def __init__(self):
        self.color = 0xFF0000       # 차 색상
        self.wheel_size = 18        # 휠 사이즈
        self.displacment = 2000     # 배기량

    def forward(self):
        pass

    def backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

my_car = Car()
pcs_car = Car()

print('type of my_car', type(my_car))
print('type of pcs_car', type(pcs_car))

print('내차 배기량 : ', my_car.displacment)
print('psc차 배기량 : ', pcs_car.displacment)

class temp:
    a = None

    def __init__(self, dosi): #객체가 만들어질 때 반드시 실행되는 메서드
        self.a = dosi

    def driving(self, dosi):
        print('%s로 운전 중입니다.' % (dosi))

seowool = temp('서울대입구')
print('도착지 : ', seowool.a)
seowool.driving('남극으')



'''
public class Test {
    int age;
    String name;
    void abc(){
    }
    public Test(){
        super();
    }
}
'''
