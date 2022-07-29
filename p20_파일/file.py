class FilePath:
    #final
    FILE_PATH = "C:/junil/junil/python_20220707/fileupload/"

    fileName = None

    def __init__(self, fileName):
        self.fileName = fileName

    def getOpenFilePath(self):
        return self.FILE_PATH + self.fileName

class File:
    filePath = None
    fileName = None
    encoding = "utf8"

    def __init__(self, fileName):
        self.fileName = fileName
        self.filePath = FilePath(fileName).getOpenFilePath()

    def openFile(self, accessMode, defaultData=None):
        file = None
        try:
            file = open(self.filePath, accessMode, encoding=self.encoding)
        except FileNotFoundError as e:
            print("해당 파일이 존재하지 않아 기본파일을 생성합니다.")
            file = open(self.filePath, "w", encoding=self.encoding)
            file.write(defaultData)
            file.close()
            file = open(self.filePath, accessMode, encoding=self.encoding)
        return file

    def closeFile(self, file):
        file.close()









