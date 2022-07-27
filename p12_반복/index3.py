numbers = list()

"""
반복할 횟수를 입력하세요: 10
"""
n = int(input("반복 할 횟수를 입력하세요: "))

i = 0
while i < n:
    i = i + 1
    numbers.append(i)

print(f"리스트: {numbers}")

i = 0
numbers.clear()

while i < n:
    numbers.append(n - i)
    i = i + 1

print(f"리스트: {numbers}")










