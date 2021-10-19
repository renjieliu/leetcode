class Solution:
    def minimumDeletions(self, s: str) -> int:
        hmp = {}
        for i, c in enumerate(s):
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(i)
        if 'a' not in hmp or 'b' not in hmp:
            return 0
        else:
            if hmp['b'][0] > hmp['a'][-1]:
                return 0

            def binSearch(arr, target):
                s = 0
                e = len(arr) - 1
                while s <= e:
                    mid = (s + e) // 2
                    if arr[mid] > target:
                        e = mid - 1
                    else:
                        s = mid + 1
                return s

            res_a = []
            res_b = []
            lst_b = hmp['b']
            lst_a = hmp['a']
            for i in range(len(lst_b)):  # how many a and b needs to be taken out, if plug in the current b in a
                loc = binSearch(lst_a, lst_b[i])
                res_b.append(len(lst_a) - loc + i)  # all the remaining a need to be taken out + front b's

            for i in range(len(lst_a)):  # how many a and b needs to be taken out, if plug in the current a in b
                loc = binSearch(lst_b, lst_a[i])
                res_a.append(len(lst_b) + i)  # all the front a's to be taken out, plus the front b's

            return min(min(res_a), min(res_b))







