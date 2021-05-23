class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1 << N)]
        parent = [[None] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1 << N) - 1
        i = max(range(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)


# my solution, which did not work
# class Solution:
#     def shortestSuperstring(self, words: List[str]) -> str:
#         hmp = {} #to find all the words can use current one as a lead
#         for w in words:
#             hmp[w] = []
#             for w2 in words:
#                 if w2 != w:
#                     for i in range(len(w)):
#                         if w[-i:] == w2[:i]:
#                             hmp[w].append([w2, i])

#         lst = list(hmp.keys())
#         leading_words = []
#         for k in lst:
#             if hmp[k] == []: #the word cannot be a lead word
#                 del hmp[k]
#             else:
#                 leading_words.append(k) #the word to be leading word

#         def helper(seen, hmp, word, curr, output, leading_words, pool, additional):
#             if len(seen) == len(leading_words) + additional: #if not all the words are leading
#                 curr += ''.join(list(pool - seen))
#                 print(curr)
#                 if len(curr) < output[0]:
#                     output[0] = len(curr)
#                     output[1] = curr

#             elif word in hmp:
#                 for v, length in hmp[word]:
#                     if v not in seen:
#                         seen.add(v)
#                         helper(seen, hmp, v, curr+v[length:], output, leading_words, pool, additional)
#                         seen.remove(v)
#         if leading_words == []:
#             return "".join(words)

#         output = [float('inf'), ""]
#         pool = set(words)
#         additional = 1 if len(pool)!=len(leading_words) else 0
#         for word in leading_words:
#             curr = word
#             helper(set([word]), hmp, word, curr, output, leading_words, pool, additional)

#         return output[1]



