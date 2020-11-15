class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        else:
            hmp_a = {}
            hmp_b = {}
            for i in range(len(word1)):
                a = word1[i]
                b = word2[i]
                if a not in hmp_a:
                    hmp_a[a] = 0
                hmp_a[a] += 1
                if b not in hmp_b:
                    hmp_b[b] = 0
                hmp_b[b] += 1

            if len(hmp_a) != len(hmp_b):
                return False
            else:
                a_v = sorted(hmp_a.values())
                b_v = sorted(hmp_b.values())
                a_k = sorted(hmp_a.keys())
                b_k = sorted(hmp_b.keys())
                return a_k == b_k and a_v == b_v




