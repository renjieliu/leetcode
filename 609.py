def findDuplicate(paths: 'List[str]'):
    map = {}
    output = []

    for i in paths:
        folder = i.split(" ")[0] + "/"
        files = i.split(" ")[1:]
        for j in files:
            content = j.split("(")[1].replace(")","")
            fileName = j.split("(")[0]
            fullpath  = folder  + fileName
            if content not in map:
                map[content] =[]
            map[content].append(fullpath)

    for k,v in map.items():
        if len(v) >1:
            temp = []
            for x in v:
                temp.append(x)

            output.append(temp)

    return output

print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(esfgh)"]))