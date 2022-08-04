from p21_데이터베이스.repositody.UserRepository import UserRepository

class UserController:

    userRepository = None

    def __init__(self):
        self.userRepository = UserRepository()

    def addUser(self):
        print("[ 회원 추가 ]")
        username = input("아이디: ")
        password = input("비밀번호: ")
        name = input("이름: ")
        email = input("이메일: ")
        userDict = {
            "username": username,
            "password": password,
            "name": name,
            "email": email
        }

        self.userRepository.save(userDict)


    def getUserList(self):

        userList = self.userRepository.getUserListAll()
        for user in userList :
            print(f"""
사용자코드 > {user.get("user_code")} 
아이디\t\t > {user.get("user_id")}
비밀번호\t > {user.get("user_password")}
이름\t\t > {user.get("user_name")}
이메일\t\t > {user.get("user_email")}
주소\t\t > {user.get("user_address")}
연락처\t\t > {user.get("user_phone")}
성별\t\t > {user.get("gender_name")}
나이\t\t > {user.get("user_age")}
            """)

    def getUserByUsername(self):
        username = input("아이디: ")


    def modifyUserPhone(self):
        pass

    def removeUser(self):
        pass