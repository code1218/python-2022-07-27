# 대입 연산자
name = "김준일"

# 부호 연산자
num = 1
num = -1

# 산술 연산자
result = 10 + 2
result = 10 - 2
result = 10 * 2
result = 10 ** 2    # 제곱
result = 10 / 2
result = 10 // 2    # 몫
result = 10 % 2     # 나머지

# 비교 연산자
print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

# 논리 연산자
print(True and False)
print(True or False)
print(not (True or True))

# 복합대입 연산자(산술 연산 모두 사용가능)
num = 10
num = num + 5
num += 5
num %= 5

# 삼항(조건) 연산자
result = 0 if 10 > 5 else 1

# 윤년
# 해당 년도가 4의 배수이면서 100의 배수는 아니거나 400의 배수일 때
# 참이면 윤년입니다.
# 거짓이면 윤년이 아닙니다.

year = 2000

result = "윤년입니다." if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "윤년이 아닙니다."

print(result)





