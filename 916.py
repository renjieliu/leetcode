class Solution:
    def wordSubsets(self, A: 'List[str]', B: 'List[str]') -> 'List[str]':
        output = []
        B_dict = []

        for b in B:  # build hash table for each word in B
            B_dict.append({})
            for c in b:
                if c not in B_dict[-1]:
                    B_dict[-1][c] = 0
                B_dict[-1][c] += 1

        B_merged = {}  # to merge B

        for b in B_dict:
            for k in b.keys():
                if k not in B_merged:
                    B_merged[k] = 0
                B_merged[k] = max(B_merged[k], b[k])  # B=['a', 'aa']. then the word in A must have 'aa' in it.

        for word in A:  # create hash table for each word in A
            cnt = 0
            for k in B_merged.keys():
                if k not in word or word.count(k) < B_merged[k]:
                    break
                else:
                    cnt += 1
            if cnt == len(B_merged):
                output.append(word)

        return output
