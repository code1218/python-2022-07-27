import json
from p20_파일.file import File

fileObj = File("student.txt")

student_database = {
    "student_mst":[]
}

file = fileObj.openFile("r", json.dumps(student_database))
data = file.read()
student_database = json.loads(data)
fileObj.closeFile(file)


name = input("이름: ")
student = input("학번: ")
studentYear = input("학년: ")
age = input("나이: ")

student = {
    "name":name,
    "studentCode":student,
    "studentYear":studentYear,
    "age":age
}

file = fileObj.openFile("w")

student_mst = student_database.get("student_mst")

student_mst.append(student)
student_database.update({"student_mst":student_mst})

studentJson = json.dumps(student_database)

file.write(studentJson)

fileObj.closeFile(file)






