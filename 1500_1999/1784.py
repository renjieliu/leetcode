class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
        #return 1 == len(list(filter(lambda x: x!="" and int(x) >= 1,  s.split('0'))))