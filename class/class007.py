class Car():
    
    @staticmethod
    def check_type(model_code):
        if(model_code >=20):
            print("이 자동차는 전기차입니다.")
        elif(10 <= model_code <20):
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")

Car.check_type(25)
Car.check_type(2)