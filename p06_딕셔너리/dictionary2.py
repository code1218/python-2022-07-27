strDict = {"이름":"김준일", "나이": 29}

# key값만 리스트로 추출
print(strDict.keys())
keyList = list(strDict.keys())

# value값만 리스트로 추출
print(strDict.values())
valueList = list(strDict.values())

# key와 value를 튜플로 묶어서 추출
print(strDict.items())
itemList = list(strDict.items())

#strDict.clear()
print(strDict)

print(strDict["이름"])
print(strDict.get("이름"))

strDict.update({"이름":[1, 1, 2, 3]})
print(strDict)

strDict.update({"주소":"부산"})
print(strDict)

print(strDict.popitem())
print(strDict)









