names = [None, "김준일", "허정욱", "김병찬", "안유정", "편재윤"]

inputName = input("찾을 이름을 입력하세요: ")

searchNumber = 0

for i, name in enumerate(names):
    print(f"i -> {i}, name -> {name}")
    if name == inputName:
        searchNumber = i
        break

if names[searchNumber] != None:
    print(f"찾은 이름의 위치: {searchNumber}")