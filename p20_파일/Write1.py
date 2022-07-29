from p20_파일.file import File

fileObj = File("write1.txt")
file = fileObj.openFile("w")

file.write("안녕\n")
file.write("파이썬\n")
strList = ["김준일\n", "조부경\n", "강봉수\n"]
file.writelines(strList)
file.write("""김준일
조부경
강봉수""")

fileObj.closeFile(file)
