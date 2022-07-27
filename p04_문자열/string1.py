sss = "안녕\t하세요. \n\"김준일\"입니다."
print(sss)

print("=" * 10)

# 문자열의 길이 구하기 len()
print(len("가나다라마바사"))

# 인덱싱과 슬라이싱

strValue = "abcde"
print(strValue[1: 4])

a = "Pithon"
# 문자열을 리스트로 변환하는 방법
b = list(a)

# 리스트로 바뀐 문자열 1번 인덱스의 값에 y 대입
b[1] = 'y'
print(b)

# 리스트의 모든 값을 하나의 문자열로 합치는 방법
a = ''.join(b)
print(a)


