# 함수 내에서 전역변수를 사용하는 방법

name = "김준일"

def globalTest():
    global name
    name = "김준이"

if __name__ == "__main__":
    globalTest()
    print(name)