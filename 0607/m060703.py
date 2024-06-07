class MyClass :
    #속성
    a = 110
    b = 100

    #메서드 (함수 myclass생성시엔 a와 b에 값을 주어야하고, 각각 prop1과 prop2에 전달한다.)
    def __init__(self, a, b) :
        self.__prop1__ = a  
        self.__prop2__ = b

    def add(self) :
        return self.__prop1__ + self.__prop2__
        # return self.a + self.b
    
    def __sub__(self) :
        return self.__prop1__ - self.__prop2__

    @staticmethod
    def add2() :    #스태틱 메서드는 변수사용 불가능
        # return a + b  #클래스 멤버 a, b, __prop1__, __prop2__는 전부 객체가 생성되어 있어야 사용가능
        # return __prop1__ + __prop2__
        return 100 + 200

    @classmethod
    def add3(cls) : #cls를 필수로 가져야함
        return cls.a + cls.b
        # return cls.__prop1__ + cls.__prop2__

'''
#class 사용
# mc = MyClass()  #객체 생성할 때 __init__ 호출
mc = MyClass(5, 10)
print(mc.add())
print("기존 a값 = " , mc.a)
print("변경된 a값 = ", mc.__prop1__)
print(mc.__sub__())
'''