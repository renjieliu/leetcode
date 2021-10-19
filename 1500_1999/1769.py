class Solution:
    def minOperations(self, boxes: str) -> 'List[int]':
        pos = []
        for i, c in enumerate(boxes):
            if c=="1":
                pos.append(i)
        output = []
        for i in range (len(boxes)):
            curr = 0
            for p in pos:
                curr+= abs(p-i)
            output.append(curr)
        return output



