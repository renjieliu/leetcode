class Solution:
    def topKFrequent(self, words: 'List[str]', k: int) -> 'List[str]': # O( NlogN | N )
        cnt = defaultdict(lambda: 0) # count the frequency of the word
        for w in words:
            cnt[w] += 1 
        arr = [[k, v] for k, v in cnt.items()]
        arr.sort(key = lambda x: x[0]) # sort the word
        arr.sort(key = lambda x: x[1], reverse = True) # sort by the frequency, in descending order
        return [arr[i][0] for i in range(k)] # return the first k words




# previous solution

# def topKFrequent( words: 'List[str]', k: int):
#     map = {}
#     for i in words:
#         if i not in map:
#             map[i]= 0
#         map[i] +=1

#     values = []
#     for key,v in map.items():
#         values.append(v)
#     values.sort(reverse=1)
#     cnt = 0
#     output = []
#     while cnt < k:
#         t = []
#         for key, v in map.items():
#             if v==values[cnt] and key not in output:
#                 t.append(key)
#         curr = 0
#         for j in sorted(t):
#             output.append(j)
#             curr+= 1
#             if len(output) ==k:
#                 return output
#         cnt += curr
#     return output

# print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
# print(topKFrequent( ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
# print(topKFrequent( ["i", "love", "leetcode", "i", "love", "coding"], 3)) # ["i","love","coding"]




