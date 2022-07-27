membership = "gold"
year = 4

if membership == "vip" and year > 4:
    print("이벤트 참여 가능합니다.")
elif membership == "gold" and year > 2:
    print("이벤트 참여 3시간 가능합니다.")
else:
    print("이벤트 참여 불가능합니다.")

x = 2
y = -5

if x > 0 and y > 0 :
    print("1사분면")
elif x < 0 and y > 0 :
    print("2사분면")
elif x < 0 and y < 0 :
    print("3사분면")
else:
    print("4사분면")

score = 85
grade = ""

"""
score점수가 0보다 작거나 100보다 크면
계산 할 수 없는 점수입니다. 출력

100 ~ 90 이면 grade A학점 
80 ~ 89 이면 grade B학점 
70 ~ 79 이면 grade C학점 
60 ~ 69 이면 grade D학점 
나머지는 grade F학점

"""
if score < 0 or score > 100:
    print("계산 할 수 없는 점수입니다.")
elif score > 89:
    grade = "A학점"
elif score > 79:
    grade = "B학점"
elif score > 69:
    grade = "C학점"
elif score > 59:
    grade = "D학점"
else:
    grade = "F학점"

print(grade)










