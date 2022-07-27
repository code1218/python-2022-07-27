class UserEntity:

    user_code = None
    username = None
    password = None
    user_name = None
    user_email = None

    def __init__(self, user_code=None, username=None, password=None, user_name=None, user_email=None):
        self.user_code = user_code
        self.username = username
        self.password = password
        self.user_name = user_name
        self.user_email = user_email

    def toString(self):
        return f"""[UserEntity]
user_code: {self.user_code} 
username: {self.username} 
password: {self.password}
user_name: {self.user_name}
user_email: {self.user_email}
"""
