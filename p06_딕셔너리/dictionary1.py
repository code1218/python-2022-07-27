strDict = {"이름":"김준일", "나이":29}
strList = ["김준일", 29]

print(strDict)

print(type(strDict["이름"]))
print(type(strDict["나이"]))
print(strList[0])
print(strList[1])

strDict["주소"] = "부산 동래구"
print(strDict)

strDict["나이"] = 30
print(strDict)

# 딕셔너리의 특징
# Key값은 중복이 되지 않는다.
# 하지만 Value는 중복이 가능하다.

strDict["닉네임"] = "김준일"
print(strDict)

del strDict["주소"]
print(strDict)

# 리스트를 Key로 사용할 수 없는 이유

strDict = {1:10, "김":"김준일", (10, 20):"리스트"}
print(strDict[1])
print(strDict["김"])
print(strDict[(10, 20)])













