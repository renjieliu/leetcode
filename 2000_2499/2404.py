class Solution:
    def mostFrequentEven(self, nums: 'List[int]') -> int: # O( N | N )
        counter = defaultdict(lambda: 0)
        curr = -float('inf')
        cnt = -1
        output = -1 
        for n in nums: #count the number occurrence, if it's even.
            if n % 2 == 0:
                counter[n] += 1
                if counter[n] > cnt:
                    cnt = counter[n]
                    output = n
                    curr = n
                elif counter[n] == cnt and n < curr:
                    curr = n
                    output = n
        return output

    
    
