from UserManagementProgram.views.mainView import MainView
from UserManagementProgram.views.signupView import SignupView
from UserManagementProgram.views.signinView import SigninView
from UserManagementProgram.service.userService import UserService

class PageController:

    mainView = None
    signupView = None
    signinView = None

    userService = None

    def __init__(self):
        self.mainView = MainView()
        self.signupView = SignupView()
        self.signinView = SigninView()
        self.userService = UserService()

    def index(self):
        self.mainView.showMainDisplay()
        return input("select Menu >> ")

    def signup(self):
        userDto = self.signupView.showSignupDisplay()
        self.userService.addUser(userDto)
        # 값이 잘 들어 갔는지 확인
        self.userService.getUser(userDto.username)

    def showUserList(self):
        userList = self.userService.getUserListAll()
        self.mainView.showUserListDisplay(userList)

    def signin(self):
        username, password = self.signinView.showSigninDisplay()
        self.userService.login(username, password)










