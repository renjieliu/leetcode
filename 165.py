def compareVersion(version1: str, version2: str) -> int:
    arr_1 = version1.split(".")
    arr_2 = version2.split(".")
    diff = abs(len(arr_1) - len(arr_2))
    if len(arr_1)<len(arr_2):
        j = 0
        while j<diff:
            arr_1.append("0")
            j+=1
    else:
        arr_2.append(0*diff)
        j = 0
        while j<diff:
            arr_2.append("0")
            j+=1

    e_cnt = 0
    for i in range(len(arr_1)):
        if int(arr_1[i]) > int(arr_2[i]):
            return 1

        elif int(arr_1[i]) <int(arr_2[i]):
            return -1

        elif int(arr_1[i]) == int(arr_2[i]):
            e_cnt +=1

    if e_cnt == len(arr_1):
        return 0

    return 1

print(compareVersion("0.1", "1.1"))
print(compareVersion("1.0.1", "1"))
print(compareVersion("0.1", "1.1"))
print(compareVersion("1.01", "1.001"))
print(compareVersion("1.0", "1.0.0"))
print(compareVersion("1", "1.1"))
print(compareVersion("1.0", "0.1"))

