from UserManagementProgram.repository.userEntity import UserEntity

class UserDto:

    username = None
    password = None
    name = None
    email = None

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def toEntity(self):
        userEntity = UserEntity(username=self.username, password=self.password, user_name=self.name, user_email=self.email)
        return userEntity;

    def toString(self):
        return f"""[UserDto] 
username: {self.username} 
password: {self.password}
name: {self.name}
email: {self.email}
"""