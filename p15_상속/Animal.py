"""
오버라이드(재정의)
"""


class Animal:

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
    human = Human()
    tiger = Tiger()
    animals = [human, tiger]

    for animal in animals:
        animal.move()
        if type(animal) == "Human":
            animal.readBooks()
        elif type(animal) == "Tiger":
            animal.hunting()

    human.move()
    tiger.move()

    human.readBooks()
    tiger.hunting()










