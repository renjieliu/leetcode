class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: str) -> 'List[str]': # O( N*L | N*L ), L is the length of pattern
        def match(s1, s2):
            mapping_1 = {} # map s1 to s2 
            mapping_2 = {} # map s2 to s1
            for i in range(len(s1)):
                a = s1[i]
                b = s2[i]
                if a not in mapping_1 and b not in mapping_2:
                    mapping_1[a] = b
                    mapping_2[b] = a
                elif a in mapping_1 and b in mapping_2: #if both exist, both should be same
                    if (mapping_1[a] != b or mapping_2[b] != a): 
                        return False 
                else: # one of them is not in the hashmap, which should not happen.
                    return False
            return True 

        return [w for w in words if match(w, pattern)]
            
                    
                    
        
# previous solution 

# class Solution:
#     def findAndReplacePattern(self, words: 'List[str]', pattern: str) -> 'List[str]':
#         output = []
#         for w in words:  #if str a --> pattern b, pattern b --> str a
#             hmp_a = {} #from string, map to pattern
#             hmp_b = {} #from pattern, map to string
#             good = 1
#             for i in range(len(w)):
#                 if pattern[i] not in hmp_a and w[i] not in hmp_b:
#                     hmp_a[pattern[i]] = w[i]
#                     hmp_b[w[i]] = hmp_a[pattern[i]]
#                 elif pattern[i] not in hmp_a or w[i] not in hmp_b or hmp_a[pattern[i]] != w[i] or hmp_b[w[i]] != hmp_a[pattern[i]]:
#                     good = 0
#                     break
#             if good == 1:
#                 output.append(w)
#         return output


