class Solution:
    def singleDivisorTriplet(self, nums: 'List[int]') -> int: # TBD
        hmp = defaultdict(lambda:0)
        for n in nums:
            if n not in hmp:
                hmp[n] = 0 
            hmp[n] += 1 
        
        fact = lambda x: 1 if x == 0 or x == 1 else (x * fact(x-1))
        perm2 = lambda x: fact(x)//(fact(x-2) * 2)
        
        def valid(arr):
            s = sum(arr)
            return (s % arr[0] == 0 and s % arr[1] != 0  and s % arr[2] != 0)\
        or (s % arr[1] == 0 and s % arr[0] != 0 and s % arr[2] != 0)\
        or (s % arr[2] == 0 and s % arr[0] != 0 and s % arr[1] != 0)
        
        def combo(output, curr, arr, hmp): #check all the possible combinations, and count the valid triplet in the arr
            if len(curr) == 3: 
                if valid(curr):# all of them exists in the nums
                    if curr[0] == curr[1]: # [a, a, b ]
                        output[0] += (perm2(hmp[curr[0]]) * hmp[curr[2]] * 6) if hmp[curr[0]] >= 2 else 0
                    elif curr[1] == curr[2]: # [a, b, b]
                        output[0] += (perm2(hmp[curr[1]]) * hmp[curr[0]] * 6) if hmp[curr[1]] >= 2 else 0
                    else: # [a, b, c]
                        output[0] += hmp[curr[0]] * hmp[curr[1]] * hmp[curr[2]] * 6 
            else:
                for i in range(len(arr)):
                    combo(output, curr + [arr[i]], arr[i:], hmp)
        

        output = [0]
        arr = sorted(list(set(nums)))
        combo(output, [], arr, hmp)
        return output[0]
                    


