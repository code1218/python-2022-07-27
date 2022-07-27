strValue = "hello, python"

# 문자열에 해당 문자가 몇개인지 확인하는 함수
print(strValue.count("l"))

jStrValue = "/".join(strValue)
print(jStrValue)

strList = ["100", "200", "300", "400"]
strList2 = [100, 200, 300, 400]

print(";".join(strList))
# strList2에 들어 있는 정수(int) 자료형의 값들을 문자열로 변환
print(";".join(list(map(str, strList2))))
# strList에 들어 있는 문자열(String) 자료형의 값들을 정수로 변환
print(list(map(int, strList)))

# 문자열의 양쪽 끝에 있는 공백을 제거
strValue = " 코리아 아카데미 "
print(strValue.strip())

print(strValue.lstrip())
print(strValue.rstrip())

# 문자열에서 해당 문자열을 찾아서 다른 값으로 바꿔라
strValue2 = "코 리 아 아 카 데 미"
print(strValue2.replace(" ", ""))
phoneNumber = "010-9988-1916"
print(phoneNumber.replace("-", ""))

address = " 부산광역시 동래구 사직동 "
print(address)
# 부산-동래-사직
# 1. 양쪽 공백 제거
address = address.strip()
print(address)

# 2. 스페이스로 나눠서 list로 변환
address = address.split()
print(address)

# 3. 각가의 주소에서 광역시, 구, 동 replace하여 제거
address[0] = address[0].replace("광역시", "").replace("시", "")
address[1] = address[1].replace("구", "")
address[2] = address[2].replace("동", "")
print(address)

# 4. 제거되어 정리된 주소 list를 join을 통해 - 으로 연결(문자열)
address = "-".join(address)
print(address)





