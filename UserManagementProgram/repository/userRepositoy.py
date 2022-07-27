from UserManagementProgram.repository.userEntity import UserEntity

class UserRepository:
    user_mst = None
    autoIncrement = 0

    def __init__(self):
        self.user_mst = list()

    def insertUser(self, userEntity):
        user_mst_row = dict()
        self.autoIncrement += 1
        user_mst_row.update(
            {"user_code":self.autoIncrement,
            "username":userEntity.username,
            "password":userEntity.password,
            "user_name":userEntity.user_name,
            "user_email":userEntity.user_email}
        )
        self.user_mst.append(user_mst_row)

    def findUserByUsername(self, username):
        for user_mst_row in self.user_mst:
            if user_mst_row.get("username") == username:
                return UserEntity(
                    user_mst_row.get("user_code"),
                    user_mst_row.get("username"),
                    user_mst_row.get("password"),
                    user_mst_row.get("user_name"),
                    user_mst_row.get("user_email")
                )

        return None

    def getUserListAll(self):
        userList = list()

        for user_mst_row in self.user_mst:
            userEntity = UserEntity(
                user_mst_row.get("user_code"),
                user_mst_row.get("username"),
                user_mst_row.get("password"),
                user_mst_row.get("user_name"),
                user_mst_row.get("user_email")
            )
            userList.append(userEntity)

        return userList