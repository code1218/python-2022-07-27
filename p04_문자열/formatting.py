name = "김준일"
age = 29
# 일반적인 표현식을 사용한 문자열 포매팅
strValue = '%s님의 나이는 %s입니다.' % (name, age)

strValue2 = name + "님의 나이는 " + str(age) + "입니다."

strValue3 = name, "님의 나이는", age, "입니다."

print(strValue)
print(strValue2)
print(strValue3)
print(name, "님의 나이는", age, "입니다.")


