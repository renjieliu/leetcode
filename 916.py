class Solution:
    def wordSubsets(self, A: 'List[str]', B: 'List[str]') -> 'List[str]':
        def convert(w): #convert the word to hashmap
            hmp = {}
            for c in w:
                if c not in hmp:
                    hmp[c] = 0
                hmp[c]+=1
            return hmp

        B=list(set(B))
        arr_b = []
        for i in range(len(B)):
            arr_b.append(convert(B[i]))

        B_merged = {} #to merge B

        for b in arr_b:
            for k in b.keys():
                if k not in B_merged:
                    B_merged[k] = 0
                B_merged[k] = max(B_merged[k], b[k]) # B=['a', 'aa']. then the word in A must have 'aa' in it.

        output = []
        for a in A:
            curr = convert(a)
            error = 0
            for b,v in B_merged.items():
                if b not in curr or v > curr[b]:
                    error=1
                    break

            if error == 0 :
                output.append(a)
        return output



# previous approach
# class Solution:
#     def wordSubsets(self, A: 'List[str]', B: 'List[str]') -> 'List[str]':
#         output = []
#         B_dict = []
#
#         for b in B:  # build hash table for each word in B
#             B_dict.append({})
#             for c in b:
#                 if c not in B_dict[-1]:
#                     B_dict[-1][c] = 0
#                 B_dict[-1][c] += 1
#
#         B_merged = {}  # to merge B
#
#         for b in B_dict:
#             for k in b.keys():
#                 if k not in B_merged:
#                     B_merged[k] = 0
#                 B_merged[k] = max(B_merged[k], b[k])  # B=['a', 'aa']. then the word in A must have 'aa' in it.
#
#         for word in A:  # create hash table for each word in A
#             cnt = 0
#             for k in B_merged.keys():
#                 if k not in word or word.count(k) < B_merged[k]:
#                     break
#                 else:
#                     cnt += 1
#             if cnt == len(B_merged):
#                 output.append(word)
#
#         return output
