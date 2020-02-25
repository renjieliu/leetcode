class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = []
        b = []
        c = []
        i = 0
        while i < len(s):
            if s[i] == 'a':
                a.append(i)
            elif s[i] == 'b':
                b.append(i)
            elif s[i] == 'c':
                c.append(i)
            i += 1
        output = 0
        end = len(s) - 1
        while len(a) * len(b) * len(
                c) != 0:  # find the current least characters to have a b and c. [minn, maxx], everything after the maxx can form a new substring
            maxx = max(a[0], b[0], c[0])
            minn = min(a[0], b[0], c[0])
            output += (end - maxx + 1)
            if minn == a[0]:
                a.pop(0)
            elif minn == b[0]:
                b.pop(0)
            elif minn == c[0]:
                c.pop(0)
        return output

