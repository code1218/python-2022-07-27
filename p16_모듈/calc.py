def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def sub(*args):
    result = 0
    i = 0
    while(i < len(args)):
        if i == 0:
            result = args[i]
        else:
            result -= args[i]
        i += 1
    return result


if __name__ == "__main__":
    print("calc 모듈이 실행됩니다.")
    print("테스트 메세지입니다.")
    print(f"calc묘듈 name: {__name__}")
else:
    print("모듈의 역할로 실행되는 부분")










