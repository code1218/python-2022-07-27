def test(): #(a, b) 매개변수
    print("test 함수 호출")
    print("test입니다.")
    return "aaa" # 리턴값

# 매개변수와 리턴 값이 없는 함수
def test1():
    print("test1 함수 호출")

# 매개변수는 있고 리턴 값이 없는 함수
def test2(a, b, c):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")

# 매개변수는 없고 리턴 값이 있는 함수
def test3():
    return "김준일"

# 매개변수와 리턴 값이 모두 있는 함수
def test4(a, b, c):
    return f"이름: {a}, 나이: {b}, 주소: {c}"

# 아무런 동작을 하지 않는 함수
def test5():
    pass

if __name__ == "__main__":
    test1()
    test2("김", "준", "일")
    name = test3()
    print(f"이름: {name}")
    print(test4("김준일", 29, "부산 동래구"))
    test5()
