class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if v1 < v2:
            v1+=[0] * (len(v2) - len(v1))
        else:
            v2+=[0] * (len(v1) - len(v2))
        while v1 and v2:
            x = int(v1.pop(0))
            y = int(v2.pop(0))
            if x < y :
                return -1
            elif x > y :
                return 1
        return 0