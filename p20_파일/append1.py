from p20_파일.file import File

fileObj = File("append1.txt")
file = fileObj.openFile("a")

file.write("test\n")

fileObj.closeFile(file)
