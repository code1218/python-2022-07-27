# 매개변수를 여러개 입력받는 방법(튜플)
def addArgs(*args):
    for key, value in args:
        print(f"{key}: {value}")

def addArgsDict(user):
    for key in user.keys():
        print(f"key: {key}, value: {user.get(key)}")

    print()

    for key, value in user.items():
        print(f"key: {key}, value: {value}")

def addArgsDict2(**dictArgs):
    for key, value in dictArgs.items():
        print(f"key: {key}, value: {value}")


if __name__ == "__main__":
    addArgs(("이름", "김준일"), ("나이", 29), ("주소", "부산"))
    user = dict()
    user["name"] = "김준일"
    user.update({"email":"skjil1218@kakao.com", "username":"junil", "password":"1234"})
    addArgsDict(user)
    print()
    addArgsDict2(name="김준일", age=29)
