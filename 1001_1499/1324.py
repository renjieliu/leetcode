class Solution:
    def printVertically(self, s: str) -> 'List[str]':
        pool = s.split(' ')
        w = max(map(lambda x: len(x), pool))  # how many times to iterate.
        output = []
        i = 0
        while i < w:  # 1,2,3,4.. take the coresponding position from each word.
            t = ''
            for p in pool:
                if i >= len(p):
                    t += ' '
                else:
                    t += p[i]
            output.append(t)
            i += 1

        i = 0
        while i < len(output):
            output[i] = output[i].rstrip()
            i += 1
        return output
