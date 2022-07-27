numbers = input("숫자 3개 입력: ")
print(numbers.split())
print(list(map(int, numbers.split())))
a, b, c = map(int, numbers.split())
print(f"{a}, {b}, {c}")

a, b, c = map(int, input("숫자 3개 입력: ").split()[:3])
print(a + b + c)
