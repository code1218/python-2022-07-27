membership = "vip"
year = 5

if membership == "vip" and year > 4:
    print("이벤트에 참여가능합니다.")
    print(f"등급: {membership}")
    print(f"년차: {year}년")
    print(f"등급: {membership}\n년차: {year}년")
    print(f"""등급: {membership}
년차: {year}년""")

name = "김준일"
age = 29

str1 = "{0}의 나이는 {1}살입니다".format(name, age)
print(str1)
print("{0}의 나이는 {1}살입니다".format("김준일", 29))

str2 = f"{name}의 나이는 {age}살입니다"
print(str2)
print(f"{name}의 나이는 {age}살입니다")

str3 = f"""{name}의 나이는
{age}살입니다."""
print(str3)
print(f"""{name}의 나이는
{age}살입니다.""")






