"""
클래스 명: Car
변수
    company - 회사명
    model - 모델명
    color - 색상

메소드
    carInfo()
        회사명: 현대자동차
        모델명: 쏘나타
        색상: 화이트

현대자동차
쏘나타
화이트

기아
k5
블랙

기아
k8
그레이

"""
class Car:
    company = None
    model = None
    color = None

    def carInfo(self):
        print(f"회사명: {self.company}")
        print(f"모델명: {self.model}")
        print(f"색상: {self.color}")
        print()

"""
class Car:                      c1
    company = '현대자동차'
    model = '쏘나타'
    color = '화이트'

    def carInfo(self):
        print(f"회사명: {self.company}")
        print(f"모델명: {self.model}")
        print(f"색상: {self.color}")
        print()
        
class Car:                      c2
    company = 기아
    model = k5
    color = 블랙

    def carInfo(self):
        print(f"회사명: {self.company}")
        print(f"모델명: {self.model}")
        print(f"색상: {self.color}")
        print()
        
class Car:                      c3
    company = 기아
    model = k8
    color = 그레이

    def carInfo(self):
        print(f"회사명: {self.company}")
        print(f"모델명: {self.model}")
        print(f"색상: {self.color}")
        print()

"""

if __name__ == "__main__":
    c1 = Car()
    c2 = Car()
    c3 = Car()

    c1.company = "현대자동차"
    c1.model = "쏘나타"
    c1.color = "화이트"

    c2.company = "기아"
    c2.model = "k5"
    c2.color = "블랙"

    c3.company = "기아"
    c3.model = "k8"
    c3.color = "그레이"

    c1.carInfo()
    c2.carInfo()
    c3.carInfo()
















