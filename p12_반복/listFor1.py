for i in [1, 2, 3, 4, 5]:
    print(i)

a, b, c = [1, 2, 3]
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(f"i[{i}]")
    print(f"j[{j}]")

scoreList = [69, 39, 50, 60, 70]
num = 0
for score in scoreList:
    num = num + 1
    print(f"{num}번 학생의 점수는 {score}입니다.")
    if score > 59:
        print("합격")
    else:
        print("불합격")

print()

num = 0
while num < len(scoreList):
    score = scoreList[num]
    num = num + 1
    print(f"{num}번 학생의 점수는 {score}입니다.")
    if score > 59:
        print("합격")
    else:
        print("불합격")











