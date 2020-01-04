class Solution:
    def highFive(self, items: 'List[List[int]]') -> 'List[List[int]]':
        hmp= {}
        for i in items:
            if i[0] not in hmp:
                hmp[i[0]] = []
            hmp[i[0]].append(i[1])
        output= []
        for k in sorted(list(hmp.keys())): #sort the output id
            output.append([k, sum(sorted(hmp[k],reverse=1)[:5])//5]) #average of the top 5
        return output