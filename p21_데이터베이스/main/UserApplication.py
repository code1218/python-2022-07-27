from p21_데이터베이스.controller.UserContorller import UserController

if __name__ == "__main__":
    userController = UserController()

    while(True):
        print("[ 메뉴 선택 ]")
        print("1. 회원 추가")
        print("2. 회원 전체 조회")
        print("3. 회원 아이디로 검색")
        print("4. 회원 전화번호 수정")
        print("5. 회원 삭제")
        print("q. 프로그램 종료")

        select = input("메뉴를 선택하세요: ")

        if select == 'q':
            print("프로그램 종료")
            break
        elif select == '1':
            userController.addUser()
        elif select == '2':
            userController.getUserList()
        elif select == '3':
            userController.getUserByUsername()
        elif select == '4':
            userController.modifyUserPhone()
        elif select == '5':
            userController.removeUser()
        else:
            print("다시 선택하세요.")

