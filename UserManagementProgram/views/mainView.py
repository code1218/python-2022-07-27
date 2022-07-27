from UserManagementProgram.util.clear import consoleClear

class MainView:

    def __init__(self):
        pass

    def showMainDisplay(self):
        # consoleClear()
        print("-" * 30)
        print(f"|{'[ UserManagementProgram ]':^28}|")
        print(f"|{'1. signup':^28}|")
        print(f"|{'2. signin':^28}|")
        print(f"|{'3. user-list':^28}|")
        print(f"|{'q. exit':^28}|")
        print("-" * 30)

    def showUserListDisplay(self, userList):
        print("-" * 30)
        print(f"|{'[ UserManagementProgram ]':^28}|")
        for userEntity in userList:
            print(f"""userCode > {userEntity.user_code}
username > {userEntity.username}
password > {userEntity.password}
name > {userEntity.user_name}
email > {userEntity.user_email}
""")
        print("-" * 30)
