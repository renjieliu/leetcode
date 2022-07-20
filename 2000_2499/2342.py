class Solution:
    def maximumSum(self, nums: 'List[int]') -> int: # O( NlogN | N )
        def digSum(n):  # compute the sum of the digits 
            output = 0 
            while n > 0:
                output += n % 10 
                n //= 10 
            return output
        
        nums.sort() #sort the number, to avoid sort each bin later
        output = -1 
        hmp = defaultdict(lambda : [])
        for n in nums:
            t = digSum(n)
            hmp[t].append(n) # add to the bin
            if len(hmp[t]) > 1:
                output = max(hmp[t][-1]+hmp[t][-2], output)
        return output


