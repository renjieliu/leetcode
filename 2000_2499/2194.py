class Solution:
    def cellsInRange(self, s: str) -> 'List[str]':
        output = []
        r1 = s[0] # starting row
        r2 = s[-2] #ending row
        c1 = int(s[1]) #starting col
        c2 = int(s[-1]) #ending col
        for r in range(ord(r1), ord(r2)+1):
            for c in range(c1, c2+1):
                output.append(chr(r)+str(c))
        return output


