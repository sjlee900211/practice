class Bicycle(): #클래스 선언

    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0}, {1}): 정지 ".format(self.wheel_size, self.color))           
        
my_bicycle = Bicycle()

my_bicycle.wheel_size = 26
my_bicycle.color = 'black'

my_bicycle.move(20)
my_bicycle.turn("좌")
my_bicycle.stop()

bicycle1 = Bicycle()
bicycle1.wheel_size = 27
bicycle1.color = 'red'

bicycle1.move(20)
bicycle1.turn('좌')
bicycle1.stop()

bicycle2 = Bicycle()
bicycle2.wheel_size = 24
bicycle2.color = 'blue'

bicycle2.move(15)
bicycle2.turn('우')
bicycle2.stop()