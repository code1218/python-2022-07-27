from p20_파일.file import File
import json

fileObj = File("json1.txt")
file = fileObj.openFile("r")

data = file.read()

fileObj.closeFile(file)

print(data)

user = json.loads(data)

print(user.get("name"))