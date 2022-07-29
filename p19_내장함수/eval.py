userDataText = """{
        'name': 'junil',
        'age': 29,
        'address':'부산 동래구 사직동',
        'phone':'010-9988-1916'
    }"""

userDict = eval(userDataText)

print(userDict.get('name'))

def add(a, b):
    return a + b

functionText = "add(10, 20)"

print(eval(functionText))