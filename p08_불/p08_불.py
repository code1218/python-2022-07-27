#부울

# 부울 연산

# True = 1, False = 0

# and(&) - 곱
# True and True => True
# True and False => False
# False and False => False
print(True and True)
print(True and False)
print(False and False)
print("=" * 30)

# or(|) - 합
# True or True => True
# True or False => True
# False or False => False
print(True or True)
print(True or False)
print(False or False)
print("=" * 30)

# not(!) - 부정
# not True => False
# not False => True
print(not True)
print(not False)
print("=" * 30)
# 윤년
# 해당 년도가 4의 배수이면서 100의 배수는 아니거나 400의 배수일 때
year = 1999 # 윤년이 아니다
#year = 2000 # 윤년

# %연산자 나머지를 구하는 연산자

print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

"""
and연산은 모든 조건이 참일 때만 True이다
하나라도 False면 결과는 False이다

or연산은 모든 조건이 거짓일 때만 False이다
하나라도 True면 결과는 True

"""




