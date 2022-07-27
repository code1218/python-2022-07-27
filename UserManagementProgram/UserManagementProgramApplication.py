from UserManagementProgram.controller.pageController import PageController
from UserManagementProgram.views.errorView import ErrorView

if __name__ == "__main__":
    pageController = PageController()

    loopFlag = True

    while loopFlag:
        select = pageController.index()
        if select == "1":
            pageController.signup()
        elif select == "2":
            pageController.signin()
        elif select == "3":
            pageController.showUserList()
        elif select == "q":
            print("프로그램 종료중...")
            loopFlag = False
        else:
            ErrorView().showSelectError()

    print("프로그램 종료.")


