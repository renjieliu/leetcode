class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        else:
            hmp = {}
            i = 0
            while i < len(str1):
                if str1[i] not in hmp:  # if the same character need to become 2 diff, it's impossible
                    hmp[str1[i]] = str2[i]
                elif hmp[str1[i]] != str2[i]:
                    return False
                i += 1
            return True if len(set(list(str2))) < 26 else False  # if 26, we can use the repeating character as leeway.
