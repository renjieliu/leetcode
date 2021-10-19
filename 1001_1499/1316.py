class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        hmp = {}
        for i in range(len(text)):  # position for each letter
            if text[i] not in hmp:
                hmp[text[i]] = []
            hmp[text[i]].append(i)
        pool = {}
        for k, v in hmp.items():
            if len(v) < 2:
                continue
            else:
                for i in range(len(v)):
                    p1 = v[i]
                    for j in range(i + 1, len(v)):
                        p2 = v[j]
                        w = p2 - p1
                        if text[p1:p2] == text[p2: p2 + w] and text[p1:p2] not in pool:
                            pool[text[p1:p2]] = None
        return len(pool)

