def filterFuntion(dataList):
    strList = list()
    intList = list()

    for data in dataList:
        if isinstance(data, str):
            strList.append(data)
        elif isinstance(data, int):
            intList.append(data)


    return strList, intList


dataList = [1, 2, "김", "준일", 3, 4, "a", "b"]

filteringDataStrList, filteringDataIntList = filterFuntion(dataList)

print(filteringDataStrList)
print(filteringDataIntList)

def filter1(data):
    return isinstance(data, str)

filteringStrList = list(filter(filter1, dataList))

print(filteringStrList)


