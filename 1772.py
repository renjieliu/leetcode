class Solution:
    def sortFeatures(self, features: 'List[str]', responses: 'List[str]') -> 'List[str]':
        feature_order = {}
        for i, f in enumerate(features):
            feature_order[f] = i
        hmp = {}
        for f in set(features):
            hmp[f] = 0
        for r in responses:
            for c in set(r.split(' ')): #this will remove the dups
                if c in hmp:
                    hmp[c]+=1
        hmp_cnt = {} #group the items with same occurrence
        for k, v in hmp.items():
            if v not in hmp_cnt:
                hmp_cnt[v] = []
            hmp_cnt[v].append(k)
        output = []
        for k in sorted(hmp_cnt.keys(), reverse = True):
            output += sorted(hmp_cnt[k], key = lambda x: feature_order[x] )
        return output

