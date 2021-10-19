class FileSystem:

    def __init__(self):
        self.folder = {'/': []} #to store all the folder structure
        self.file = {} # to store the file content

    def parent(self, s): #to find the parent of the path
        for i in range(len(s)-1, 0, -1):
            if s[i] == "/":
                return s[:i]
        return "/"

    def name(self, s): #extract the last part of the s, as file/folder name
        output = ""
        for i in range(len(s)-1, -1,-1):
            if s[i] != '/':
                output = s[i] + output
            else:
                break
        return output


    def ls(self, path: str) -> 'List[str]':
        if path in self.file: #if the path is a file
            return [self.name(path)]
        else:
            return sorted(list(set(self.folder[path])))

    def mkdir(self, path: str) -> None:
        path_stk = [] #from curr to root
        while path and path != "/": #to add get the parent folders
            path_stk.append(path)
            path = self.parent(path)

        path_stk.append('/') #add root to the path_stk

        for i in range(len(path_stk)-2, -1, -1): # starting from the second main folder
            curr = path_stk[i]
            if curr not in self.folder:
                self.folder[curr] = []
            self.folder[path_stk[i+1]].append(self.name(curr)) #add the name to the parent folder collection

        #print(path_stk, self.folder)

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.file:
            self.folder[self.parent(filePath)].append(self.name(filePath)) # add file to the folder
            self.file[filePath] = "" # initiate the file
        self.file[filePath] += content


    def readContentFromFile(self, filePath: str) -> str:
        return self.file[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)