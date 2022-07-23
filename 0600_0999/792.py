class Solution:
    def numMatchingSubseq(self, s: str, words: 'List[str]') -> int: #O( KLogN | N ), K is the length of the longest word in words
        hmp = {}
        for i, c in enumerate(s):
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(i)
        
        
        def binFind(loc_arr, loc): # loc_arr is the location of each character in s. To find the first element in arr >= v
            output = -1
            s = 0
            e = len(loc_arr)-1

            while s <= e:
                mid = s - (s-e)//2
                if loc_arr[mid] >= loc:
                    output = loc_arr[mid]
                    e = mid - 1 
                else: 
                    s = mid + 1
            return output
        
        def helper(hmp, t): # to check if t is a subsequence of s, which has been turned to hmp
            idx = 0 
            for c in t:
                if c not in hmp:
                    return 0
                idx = binFind(hmp[c], idx) #to find if there's an c in the hmp[c], with location >= previous found

                if idx == -1:
                    return 0 
                else:
                    idx += 1 # need to advance the pointer, to be the start searching location
            return 1 
        
        cnt = 0 
        for w in words:
            cnt += helper(hmp, w)
        return cnt
                
                
                
                
                

# previous solution

# class Solution:
#     def numMatchingSubseq(self, s: str, words: 'List[str]') -> int:
#         def isSub(a, b):
#             i = 0
#             while True:
#                 t = a.find(b[i])
#                 if t == -1:
#                     return 0
#                 a = a[t+1:]
#                 i += 1
#                 if i == len(b):
#                     return 1
#             return 0

#         output = 0
#         for w in words:
#             output += 1 if isSub(s, w) else 0
#         return output


# previous approach
# def numMatchingSubseq(S: str, words: 'List[str]'):
#     cnt = 0
#     for i in words:
#         t = S
#         ok = 0
#         for w in i:
#             if t.find(w) == -1:
#                 break
#             else:
#                 t = t[t.index(w) + 1:]
#                 ok += 1
#
#         if ok == len(i):
#             cnt += 1
#
#     return cnt
#
#
# print(numMatchingSubseq("abcde",  ["a", "bb", "acd", "ace"]))


