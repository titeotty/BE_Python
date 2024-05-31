class MyClass:
    # 클래스 속성
    p1 = 100

    def __init__(self, a, b):
        # 생성자: 인수 두 개를 받아 인스턴스 속성에 할당
        self.a = a
        self.b = b

    def __init__(self, a, b) :
        a = 1000
        b = 2000
        self.a = a
        self.b = b

    # 메서드
    def add(self):
        # 인스턴스 속성 a와 b를 더하여 반환
        return self.a + self.b
    

# 클래스 사용
instance1 = MyClass(3, 5)  # 첫 번째 인스턴스 생성
instance2 = MyClass(10, 20)  # 두 번째 인스턴스 생성

# 메서드 호출 (인스턴스1 사용)
print(instance1.a)
print(instance1.b)
print(instance1.add())

instance1.p1 += 100
print(instance1.p1)

print(instance2.p1)
print(MyClass.p1)
print(MyClass.__init__)