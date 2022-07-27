# 매개변수 명을 지정하여 호출하는 방법

def showInfo(name, email, username, password="0000"):
    print(f"name: {name}")
    print(f"email: {email}")
    print(f"username: {username}")
    print(f"password: {password}")


if __name__ == "__main__":
    showInfo("김준일", "skjil1218@kakao.com", "junil", "1234")
    showInfo(username="aaa", email="aaa@naver.com", name="준일")