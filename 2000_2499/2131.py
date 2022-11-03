class Solution:
    def longestPalindrome(self, words: 'List[str]') -> int: # O( N | N )
        hmp_1 = defaultdict(lambda: 0) # for the words with different letters
        hmp_2 = defaultdict(lambda: 0) # for the words with same letters
        
        for w in words: # count the occurrence of each word
            if w[0] == w[1]:
                hmp_2[w] += 1 
            else:
                hmp_1[w] += 1 
        
        output = 0
        mx = 0
        arr = [v for k, v in hmp_2.items() if v % 2] # find odd occurrence in the same letter group, the max occurrence to be placed in middle
        if arr:
            mx = max(arr)
        
        mx_taken = 0 # the max is not taken
        for k, v in hmp_2.items():
            if v == mx and mx_taken == 0 :  #take all, if it's the max odd occurrence
                output += v*2
                mx_taken = 1 
            else: # take the closest even times, and *2 for the total length added
                output += 2*(v//2)*2 
        
        used = set()
        for k, v in hmp_1.items():
            if k[::-1] in hmp_1 and k[::-1] not in used: # the word is not used yet
                used.add(k)
                used.add(k[::-1])
                output += min(hmp_1[k], hmp_1[k[::-1]]) * 4 # one group is 4 letters.

        return output







# previous solution

# class Solution:
#     def longestPalindrome(self, words: 'List[str]') -> int: # O( N | N )
#         hmp_1 = defaultdict(lambda: 0) # for the words with different letters
#         hmp_2 = defaultdict(lambda: 0) # for the words with same letters
        
#         for w in words: # count the occurrence of each word
#             if w[0] == w[1]:
#                 hmp_2[w] += 1 
#             else:
#                 hmp_1[w] += 1 
        
#         output = 0
#         mx = 0
#         arr = [v for k, v in hmp_2.items() if v % 2] # find odd occurrence in the same letter group, the max occurrence to be placed in middle
#         if arr:
#             mx = max(arr)
        
#         mx_taken = 0 # the max is not taken
#         for k, v in hmp_2.items():
#             if v == mx and mx_taken == 0 :
#                 output += v*2
#                 mx_taken = 1 
#             else:
#                 output += 2*(v//2)*2 # for the odd occurrence, it will take the closest even times, and for the even times, it will take all
        
#         used = set()
#         for k, v in hmp_1.items():
#             if k[::-1] in hmp_1 and k[::-1] not in used:
#                 used.add(k)
#                 used.add(k[::-1])
#                 output += min(hmp_1[k], hmp_1[k[::-1]]) * 4 # one group is 4 letters.

#         return output




