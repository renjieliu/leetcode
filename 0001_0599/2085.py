class Solution:
    def countWords(self, words1: 'List[str]', words2: 'List[str]') -> int:
        def helper(hmp, w):
            for c in w:
                hmp[c] += 1 
        hmp_1 = defaultdict(lambda:0) 
        hmp_2 = defaultdict(lambda:0) 
        helper(hmp_1, words1)
        helper(hmp_2, words2)
        cnt = 0 
        for k, v in hmp_1.items():
            cnt += 1 if v == hmp_2[k] == 1 else 0
        return cnt 
    

