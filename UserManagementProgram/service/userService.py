from UserManagementProgram.repository.userRepositoy import UserRepository

class UserService:

    userRepository = None

    def __init__(self):
        self.userRepository = UserRepository()

    def addUser(self, userDto):
        self.userRepository.insertUser(userDto.toEntity())

    def getUser(self, username):
        userEntity = self.userRepository.findUserByUsername(username)
        if userEntity != None:
            print(userEntity.toString())

    def getUserListAll(self):
        userList = self.userRepository.getUserListAll()
        return userList

    def login(self, username, password):

        from UserManagementProgram.util.exception.usernameNotFoundError import UsernameNotFoundException
        from UserManagementProgram.util.exception.passwordError import PasswordErrorException

        userEntity = self.loadUserByUsername(username)

        try:
            if userEntity == None:
                raise UsernameNotFoundException("해당 사용자 이름은 존재하지 않습니다.")
            else:
                if password != userEntity.password:
                    raise PasswordErrorException("비밀번호를 확인해 주세요.")
                    # PasswordErrorException
                else:
                    print("로그인 성공")
        except UsernameNotFoundException as e:
            print("사용자 이름을 찾지 못함")
        except PasswordErrorException as e:
            print(e)
        except Exception as e:
            print(f"Error Message >> {e.__class__}:{e}")


    def loadUserByUsername(self, username):
        userEntity = self.userRepository.findUserByUsername(username)
        if userEntity == None:
            return None
        return userEntity











