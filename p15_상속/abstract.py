from abc import *

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("사람이 두발로 걷습니다.")

    def readBooks(self):
        print("사람이 책을 읽습니다.")

class Tiger(Animal):

    def move(self):
        print("호랑이가 네발로 뜁니다.")

    def hunting(self):
        print("호랑이가 사냥을 합니다.")


if __name__ == "__main__":
    # animal = Animal()
    # animal.move()

    human = Human()
    human.move()

    tiger = Tiger()
    tiger.move()














