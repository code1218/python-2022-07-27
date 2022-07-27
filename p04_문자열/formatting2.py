# 포맷함수를 사용한 문자열 포매팅
name = "김준일"
age = 29

strValue = "{name}님의 나이는 {age}입니다.".format(name=name, age=age)
print(strValue)

strValue2 = f"{name}님의 나이는 {age}입니다.{name}"
print(strValue2)

