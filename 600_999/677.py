class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmp = {}
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        prev = 0
        if key not in self.hmp:
            self.hmp[key] = val
        else:
            prev = self.hmp[key]
            self.hmp[key] = val

        curr = self.trie
        for k in key:
            if k not in curr:
                curr[k] = [0, {}]
            curr[k][0] += (val - prev)
            curr = curr[k][1]
            #print(self.trie)

    def sum(self, prefix: str) -> int:
        curr = self.trie
        findLetter = 0
        score = 0
        for p in prefix:
            if p not in curr:
                return 0
            else:
                findLetter += 1
                score = curr[p][0]
                curr = curr[p][1]

        return score if findLetter == len(prefix) else 0




# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


# previous approach

# class MapSum:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hash = {}
#
#     def insert(self, key: str, val: int) -> None:
#         self.hash[key] = val
#
#     def sum(self, prefix: str) -> int:
#         output = 0
#         for k, v in self.hash.items():
#             if k.find(prefix) == 0:
#                 output += v
#         return output
#
# # Your MapSum object will be instantiated and called as such:
# # obj = MapSum()
# # obj.insert(key,val)
# # param_2 = obj.sum(prefix)