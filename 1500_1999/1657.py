class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool: # O( N | N )
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        counter_1 = defaultdict(lambda: 0)
        counter_2 = defaultdict(lambda: 0)
        for a, b in zip(word1, word2): # record the number of letter occurrence
            counter_1[a] += 1
            counter_2[b] += 1

        times_count_1 = defaultdict(lambda: 0) # record the count of each occurrence
        times_count_2 = defaultdict(lambda: 0)
        
        for k, v in counter_1.items():
            times_count_1[v] += 1
        for k, v in counter_2.items():
            times_count_2[v] += 1 
        
        for k, v in times_count_1.items(): # count of occurrence should match with the other one 
            if k not in times_count_2 or times_count_2[k] != v:
                return False

        return True





# previous solution

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1)!= len(word2):
#             return False
#         else:
#             arr_a = [0]*26 #to hold occurrence of characters
#             arr_b = [0]*26
#             word2 = list(word2)
#             base = ord('a')
#             for i, c in enumerate(word1):
#                 arr_a[ord(c)-base ]+=1
#                 arr_b[ord(word2[i])-base]+=1
#             if set(arr_a)!=set(arr_b): #the occurrence numbers needs to be same for them to be close
#                 return False
#             else:
#                 while arr_a and arr_b:
#                     a = arr_a.pop(0)
#                     b = arr_b.pop(0)
#                     if a*b == 0 and a+b != 0: #one of them is zero
#                         return False
#                 return True



# previous solution

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False
#         else:
#             hmp_a = {}
#             hmp_b = {}
#             for i in range(len(word1)):
#                 a = word1[i]
#                 b = word2[i]
#                 if a not in hmp_a:
#                     hmp_a[a] = 0
#                 hmp_a[a] +=1
#                 if b not in hmp_b:
#                     hmp_b[b] = 0
#                 hmp_b[b] += 1
            
#             if len(hmp_a) != len(hmp_b):
#                 return False 
#             else:
#                 a_v = sorted(hmp_a.values())
#                 b_v = sorted(hmp_b.values())
#                 a_k = sorted(hmp_a.keys())
#                 b_k = sorted(hmp_b.keys())
#                 return a_k == b_k and a_v == b_v
                
                
                