str1 = "안녕"

i = 0
try:
    i = str1.index("하")
    print(i)

except IndexError as e:
    print("예외가 발생했어")
    print(e)
except Exception as e:
    print("모든 예외 처리")
    print(e)
finally:
    print("예외가 일어나든 일어나지 않든 항상 꼭 실행되어야한다.")


print("프로그램 실행 중...")


print("아직 프로그램이 종료되지 않았는데...")