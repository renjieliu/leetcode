class FileSystem:

    def __init__(self): # O(1 | 1)
        self.hmp = {}
        

    def createPath(self, path: str, value: int) -> bool:  # O(N | N)
        if path in self.hmp:  #itself is already in the system
            return False
        
        arr = path[1:].split('/') # take out the first /
        curr = ""
        for a in arr[:-1]:  # check all the parent folder, and do not include itself. 
            curr += "/" + a
            if curr not in self.hmp:
                return False
        self.hmp[path] = value
        return True
        

    def get(self, path: str) -> int: # O(1 | 1)
        return self.hmp[path] if path in self.hmp else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


