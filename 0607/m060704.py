#m060703.py 모듈을 사용
from m060703 import MyClass

mc1 = MyClass(10, 20)
print(mc1.add())
print("기존 a값 = ", mc1.a)
print("변경된 a값 = ", mc1.__prop1__)
print(mc1.__sub__())

#파이썬 클래스 멤버 이름이 __로 시작하면 private, _로 시작하면 protected, 이름에 _가 없으면 public

# MyClass.add()

print(MyClass.add2())   #static 메서드 사용
#static 메서드는 클래스 이름으로 사용

# prop가 없기 때문에 이렇게 호출 불가능
# print(MyClass.add3())

mc2 = MyClass(1000, 2000)   #클래스 메서드 사용
print(mc2.add3())