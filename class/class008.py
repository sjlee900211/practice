class Car():
    instansce_count = 0
    
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instansce_count = Car.instansce_count + 1
        
        
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {0}".format(cls.instansce_count))

Car.count_instance()

car1 = Car("small", "red")
Car.count_instance()

car2 = Car("big", "green")
Car.count_instance()