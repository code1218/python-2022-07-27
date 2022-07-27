"""
    클래스명은 무조건 대문자로 시작한다.
    클래스는 변수(속성)과 메소드(기능)을 포함 할 수 있다.
"""
# Animal 클래스 정의
class Animal:
    name = None

    # move()메소드 정의
    def move(self):
        print("동물이 움직입니다.")

    def getName(self):
        return self.name

"""
객체 주소(힙메모리에서 빌린 주소) 주소: 100
class Animal:
    name = None

    # move()메소드 정의
    def move(self):
        print("동물이 움직입니다.")

    def getName(self):
        return self.name

"""


#Animal 객체를 생성후 animal 변수에 객체를 대입
animal = Animal() # 인스턴스(instance)
print(f"animal 객체 주소: {id(animal)}")

animal2 = Animal()
print(f"animal2 객체 주소: {id(animal2)}")

print()

#animal 객체의 move() 메소드를 호출
animal.move()
animal2.move()

animal.name = "콩이"
animal2.name = "깜순이"

print(f"우리집 강아지의 이름은 {animal.getName()}입니다.")
print(f"우리집 강아지의 이름은 {animal2.getName()}입니다.")











