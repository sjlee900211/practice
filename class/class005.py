class Car2():
    count = 0
    
    def __init__(self, size, num):
        self.size = size
        self.count = num
        Car2.count = Car2.count + 1
        print("자동차 객체의 수: Car2.count = {0}".format(Car2.count))
        print("인스턴스 변수 초기화: self.count = {0}".format(self.count))
        
    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.count))

car1 = Car2("big", 20)   
car2 = Car2("small", 30)