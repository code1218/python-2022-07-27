from p20_파일.file import File
import json

user = {
    "username": "junil",
    "password": "1234",
    "name": "김준일",
    "email": "skjil1218@kakao.com",
    "hobby": ["골프", "축구", "농구"]
}

jsonText = json.dumps(user)

print(jsonText)

jsonObj = json.loads(jsonText)

print(jsonObj.get("hobby")[0])


fileObj = File("json1.txt")
file = fileObj.openFile("w")

file.write(json.dumps(user))

fileObj.closeFile(file)
