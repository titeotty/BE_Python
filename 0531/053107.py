#import 하는 순간, print() 함수가 실행된다.
from modules.m053108 import msg as msginmodule

if __name__ == "__main__":
    msg = "같은 이름의 변수가 있다."
    
    print(msg)
    print(msginmodule)
    print(__name__)