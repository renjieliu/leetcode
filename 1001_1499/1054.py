class Solution:
    def rearrangeBarcodes(self, barcodes: 'List[int]') -> 'List[int]':
        hmp = {}
        for b in barcodes:
            if b not in hmp:
                hmp[b] = []
            hmp[b].append(b)
        pool = sorted(hmp.values(), key =lambda x: len(x), reverse = True)
        temp = []
        for p in pool:
            for c in p:
                temp.append(c)
        i = temp[:len(temp)//2]
        j = temp[len(temp)//2:]
        output = []
        while i:
            output.append(i.pop())
            if j :
                output.append(j.pop())
        if i:
            output.append(i.pop())
        if j:
            output.append(j.pop())
        return output