"""
클래스명: Student
변수
        studentCode(학번)
        studentName(이름)
        studentYear(학년)
        studentAddress(주소)
        studentPhone(연락처)

메소드
        studentInfo():
            학번:
            이름:
            학년:
            주소:
            연락처:

"""
from _ast import stmt


class Student:
    studentCode = None
    studentName = None
    studentYear = None
    studentAddress = None
    studentPhone = None

    def studentInfo(self):
        print(f"학번: {self.studentCode}")
        print(f"이름: {self.studentName}")
        print(f"학년: {self.studentYear}")
        print(f"주소: {self.studentAddress}")
        print(f"연락처: {self.studentPhone}")
        print()


if __name__ == "__main__":
    student1 = Student()
    student2 = Student()
    student3 = Student()

    student1.studentCode = 20220001
    student1.studentName = "김준일"
    student1.studentYear = 2
    student1.studentAddress = "부산 동래구"
    student1.studentPhone = "010-9988-1916"

    student1.studentInfo()
    student2.studentInfo()
    student3.studentInfo()















