a = 5 #전역 변수

def func1():
    a = 1 # 지역 변수. func1()에서만 사용
    print("[func1] 지역 변수 a =", a)
    
def func2():
    a = 2 # 지역 변수. func2()에서만 사용
    print("[func2] 지역 변수 a =", a)
    
def func3():
    print("[func3] 전역 변수 a =", a)
    
def func4():
    global a # 함수 내에서 전역 변수 변경을 위해 선언
    a = 4   # 전역 변수의 값 변경
    print("[func4] 전역 변수 a =", a)
    
func1() #함수 호출
func2()
print("전역 변수 a = ", a) # 전역 변수 출력
func3()
func4()
func3() #func4 호출로 전역 변수 a값 변경