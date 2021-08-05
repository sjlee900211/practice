class Car():
    instance_count = 0
    
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))
        
    def move(self, speed):
        self.speed = speed
        print("자동차({0} & {1})가 ".format(self.size, self.color), end='')
        print("시속 {0}킬로미터로 전진".format(self.speed))
        
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed)
        
car1 = Car("small", "red")
car2 = Car("big", "green")

car1.move(80)
car2.move(100)

car1.auto_cruise()
car2.auto_cruise()       
        