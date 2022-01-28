class Solution:
    def rearrangeArray(self, nums: 'List[int]') -> 'List[int]':
        pos = []
        neg = []
        output = []
        for n in nums:
            if n < 0 :
                neg.append(n)
            else:
                pos.append(n)
        i = 0 
        while i < len(pos):
            output.append(pos[i])
            output.append(neg[i])
            i+= 1
        return output
    
    
