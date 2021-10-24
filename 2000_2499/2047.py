class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = "((?<![0-9])[a-z])*([a-z]-[a-z])?([a-z](?![0-9]))*([!,.])?$"
        cnt = 0 
        for a in sentence.split(' ') :
            if a and re.match(pattern, a):
                # print(a)
                cnt += 1
        return cnt



# previous approach
# class Solution:
#     def countValidWords(self, sentence: str) -> int:
#         arr = sentence.split(' ') 
#         cnt = 0 
#         for a in arr:
#             if a:
#                 valid = 1
#                 for c in a: #It only contains lowercase letters, hyphens, and/or punctuation (no digits)
#                     if 48 <= ord(c) <=57:
#                         valid = 0 
#                         break 
                
#                 if a.count('-') > 1:#There is at most one hyphen '-'. 
#                     valid = 0

#                 if a.count('-') == 1: #If present, it should be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
#                     loc = a.find('-')
#                     if not (loc > 0 and loc < len(a)-1 and 97<=ord(a[loc-1]) <=122 and 97<=ord(a[loc+1])<=122 ):
#                         valid = 0                 
                
#                 t = a.replace('.', '').replace(',','').replace('!', '')
#                 if len(a) - len(t) > 1: # at most one punctuation mark
#                     valid = 0
#                 else: #If present, it should be at the end of the token
#                     s = ".,!"
#                     for c in s:
#                         if c in a and a.find(c)!=len(a) -1:
#                             valid = 0 
#                             break
                
#                 # if valid: print(a)
#                 cnt += valid
#         return cnt 
    
    
