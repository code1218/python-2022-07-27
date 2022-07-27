class SigninView:

    def __init__(self):
        pass

    def showSigninDisplay(self):
        username = None
        password = None

        print("-" * 30)
        print(f"|{'[ signin ]':^28}|")
        username = input("username >> ")
        password = input("password >> ")
        print("-" * 30)

        return username, password