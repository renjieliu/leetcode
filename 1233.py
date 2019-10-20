def removeSubfolders(folder: 'List[str]'):
    def dfs(check, folder, curr):
        dir = folder[curr]+'/'
        for i in range(curr+1, len(folder)):
            if folder[i].count(dir) !=0 :
                check[i] = 0
            else:
                break  #if the next one is not the subfolder, return

    folder.sort()

    check = [-1 for _ in range(len(folder))]
    for i in range(len(folder)):
        if check[i] == -1:
            dfs(check, folder, i)

    output = []
    for i in range(len(check)):
        if check[i] != 0:
            output.append(folder[i])

    return output


print(removeSubfolders( folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
print(removeSubfolders( folder = ["/a","/a/b/c","/a/b/d"]))
print(removeSubfolders( folder = ["/a/b/c","/a/b/ca","/a/b/d"]))
print(removeSubfolders( folder = ["/ah/al/am","/ah/al"]))






