FILE_PATH = "c:\\junil" # 상수니까 바꾸지 마세요

class User:
    __username = None
    __password = None
    __name = None
    __email = None

    def __init__(self, username=None, password=None, name=None, email=None):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email
        print("생성자 호출?")

    def getUsername(self):
        return self.__username

    def setUsername(self, username):
        self.__username = username

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def userInfo(self):
        print(self.__username)
        print(self.__password)
        print(self.__name)
        print(self.__email)



if __name__ == "__main__":
    user1 = User(username="bbb", email="bbb@naver.com")

    user1.userInfo()
    user1.setUsername("junil")
    username = user1.getUsername()
    user1.userInfo()
    print(f"getter로 가져온 username: {username}")
