class Solution:
    def findSubstring(self, s: str, words: 'List[str]') -> 'List[int]':  # O(N * L | N * L ) N is the length of s, L is the length of words
        def compare(h1, h2): # compare the hashmaps O( L | L ) L is the length of words
            for k,v in h1.items():
                if k not in h2 or v != h2[k]:
                    return False
            return True
        
        def buildhmp(w, L): # build the hashmap for current window O( L | L ), L is the length of the word 
            output = {}
            for i in range(0, len(w)+1-L, L):
                curr = w[i:i+L]
                if curr not in output:
                    output[curr] = 0 
                output[curr] += 1
            return output
        
        hmp = {}
        for w in words:
            if w not in hmp:
                hmp[w] = 0
            hmp[w] += 1 
        
        L = len(words[0])
        
        
        output = []
        for i in range(len(s)+1-L): # go through the list, and compare each window,  O(N * L | N * L )
            curr = s[i:i+L*len(words)] 
            if compare(hmp, buildhmp(curr, L)):
                output.append(i)
  
        return output
    



# previous solution 

# class Solution:
#     def findSubstring(s: str, words: 'List[str]'):
#         if words == []:
#             return []

#         elif s == "":
#             return [] if "" not in words else [words.index("")]

#         elif len(s) < len(words) * len(words[0]):  # total lenth of the list
#             return []

#         else:
#             word_dict = {}
#             for w in words:  # build the lookup dict
#                 if w not in word_dict:
#                     word_dict[w] = 0
#                 word_dict[w] += 1

#             output = []
#             i = 0
#             width = len(words[0])
#             len_all = len(words) * width

#             while i < len(s) - len_all + 1:  # no need to check if it's shorter than the combined
#                 curr = s[i:i + len_all]
#                 j = 0
#                 shadow = word_dict.copy()

#                 while j < len(curr) - width + 1:  # check within the current window
#                     x = curr[j:j + width]
#                     # print(curr, x, shadow)
#                     if x in shadow:
#                         shadow[x] -= 1
#                         if shadow[x] == 0:
#                             del shadow[x]
#                         if shadow == {}:  # all the words are found, and the curr should also be exhausted
#                             output.append(i)
#                             break
#                     else:
#                         break  # as long as it cannot be found in the current string, it should go back to the outer loop

#                     j += width

#                 i += 1

#             return output

