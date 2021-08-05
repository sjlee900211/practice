class Bicycle():
    
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
        
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
 
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0}, {1}): 정지 ".format(self.wheel_size, self.color))
        

my_bicycle = Bicycle(26, 'black')

my_bicycle.move(30)
my_bicycle.turn('좌')
my_bicycle.stop()