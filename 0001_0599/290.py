class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = list(pattern)
        arr = str.split(' ')
        if len(pattern) != len(arr):
            return False
        else:
            hmp_p = {}
            hmp_a = {}
            for i, p in enumerate(pattern):
                # print(hmp_p, hmp_a)
                if p not in hmp_p:
                    if arr[i] not in hmp_a:
                        hmp_p[p] = arr[i]
                        hmp_a[arr[i]] = p
                    else:
                        if hmp_a[arr[i]] != p:
                            return False
                        else:
                            continue
                else:
                    if hmp_p[p] != arr[i]:
                        return False
                    else:
                        continue
            return True

