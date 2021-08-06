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
        

class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state):
        Bicycle.__init__(self, wheel_size, color)
        #super().__init__(wheel_size, color) #super()도 사용가능
        self.state = state
    
    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state = {0}".format(self.state))
        
    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state = {0}".format(self.state))

folding_bicycle = FoldingBicycle(27, 'white', 'unfolding')

folding_bicycle.move(20)
folding_bicycle.fold()
folding_bicycle.unfold()      