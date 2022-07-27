s1 = set([10, 20, 30, 40])

# 값 추가
s1.add(50)
print(s1)

# 값을 여러개 한번에 추가
s1.update([50, 60, 70, 70])
print(s1)

# 값을 해당 값을 선택 제거
s1.remove(10)
print(s1)

# 정렬된 set의 앞쪽부터 값을 하나씩 꺼냄
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())