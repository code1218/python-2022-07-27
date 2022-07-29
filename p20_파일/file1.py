from p20_파일.file import File

FILE_PATH = File("test2.txt").getOpenFilePath()

file = open(FILE_PATH, "w")

file.close()