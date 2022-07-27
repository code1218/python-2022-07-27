numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers)

# 인덱싱 [위치 번호] : 위치번호는 0부터 시작한다.
# 리스트나 튜플, 문자열에서 특정 위치의 값을
# 참조할 때 사용한다.
print(numbers[4])

# 슬라이싱 [시작 위치 번호 : 마지막 위치 다음번호]
# 리스트나 튜플, 문자열에서 해당 범위의 값을
# 모두 참조할 때 사용한다.
print(numbers[1:5])
print(numbers[3:])
print(numbers[:5])

# 역순 인덱싱, 슬라이싱
print(numbers[-3])
print(numbers[-4:])
print(numbers[:-3])
print(numbers[-5:-2])


#다양한 형태의 값을 저장하는 리스트
list1 = [10, "김준일", 3.14, [1, 2, 3, 4], 5]

list2 = list1[3]
print(list2[2])

print(list1[3][1:3])

# 연산 사용하기 ( +, * )
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)

list4 = list1 * 3
print(list4)

# 리스트, 튜플, 문자열, 딕셔너리 자료형들의 길이(크기)
# 구해주는 함수 len()

list1_size = len(list1)
list2_size = len(list2)
list3_size = len(list3)
list4_size = len(list4)
print(list1_size)
print(list2_size)
print(list3_size)
print(list4_size)

# 리스트 기본 수정, 삭제
list1 = [1, 2, 3]

# 값 수정
list1[0] = 10
list1[1] = 20
list1[2] = 30
print(list1)

# 값 삭제
del list1[1]
print(list1)

# 함수를 사용하는 방법
list1 = [1, 2, 3]
list1.append(4) # 제일 마지막에 추가해라
print(list1)

num1 = list1.pop(1)    # 해당 인덱스의 값을 꺼내라
num1 = list1.pop()     # 아무 인덱스를 넣지 않으면 마지막 값을 꺼낸다.
print(list1)
print(num1)

del list1[0]     # 해당 인덱스를 찾아서 제거해라

list1.remove(3)  # 해당 값을 찾아서 제거해라
print(list1)

list1.insert(1, 10)     # 해당 인덱스 위치에 값을 삽입
list1.insert(1, 20)
print(list1)

list1 = [1, 5, 3, 7, 4]
list1.sort()        # 정렬해라
print(list1)

list1.reverse()     # 반전(역순 나열)
print(list1)

list1.clear()       # 리스트를 비워라
print(list1)

list1 = [1, 1, 1, 1, 2, 3, 4, 4, 4]
num1Count = list1.count(1)  # 리스트에서 해당 값의 개수
print(num1Count)

num2Index = list1.index(4)
print(num2Index)

list2 = list1.copy()        # 깊은 복사: 주소안에 있는 모든 값을 복사
list1.remove(2)
print(list1)
print(list2)

list3 = list1               # 얕은 복사: 주소만 복사
list1.remove(3)
print(list1)
print(list3)

list1.extend([8, 8, 8, 8])  # 리스트에 리스트 더하기
list1 = list1 + [8, 8, 8, 8]
print(list1)

str1 = "abcdefg"
print(str1[1:4])
