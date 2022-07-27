from UserManagementProgram.dto.userDto import UserDto

class SignupView:

    def __init__(self):
        pass

    def showSignupDisplay(self):
        username = None
        password = None
        name = None
        email = None

        print("-" * 30)
        print(f"|{'[ signup ]':^28}|")
        username = input("username >> ")
        password = input("password >> ")
        name = input("name >> ")
        email = input("email >> ")
        print("-" * 30)

        return UserDto(username, password, name, email)


