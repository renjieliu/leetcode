class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool: # O(N | N)
        def compute(s): # follow the requirement, and generate the result 
            output = []
            for c in s:
                if c == "#":
                    if output:
                        output.pop()
                else:
                    output.append(c)
            return output
    
        return compute(s) == compute(t)
    

# previous solution

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         a = [] 
#         for c in S: 
#             if c== "#" and a:
#                 a.pop()
#             elif c!="#":
#                 a.append(c) 
#         b = []
#         for c in T:
#             if c == "#" and b:
#                 b.pop()
#             elif c!="#":
#                 b.append(c)
#         return a==b


# previous solution

# def backspaceCompare(S: str, T: str):
#     clean_1 = ""
#     for i in S:
#         if i == "#" and len(clean_1)>0:
#             clean_1 = clean_1[0:-1]
#         else:
#             if i != "#":
#                 clean_1 = clean_1+ i


#     clean_2 = ""
#     for i in T:
#         if i == "#" and len(clean_2)>0:
#             clean_2 = clean_2[0:-1]
#         else:
#             if i != "#":
#                 clean_2 = clean_2 + i


#     return True if clean_1 == clean_2 else False

# print(backspaceCompare("ab#c", "ad#c"))
# print(backspaceCompare("ab##", "c#d#"))
# print(backspaceCompare("a##c", "#a#c"))
# print(backspaceCompare("a#c", "b"))


