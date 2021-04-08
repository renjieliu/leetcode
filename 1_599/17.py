class Solution:
    def letterCombinations(self, digits: str) -> 'List[str]':
        hmp = {'2': ["a", "b", "c"],'3': ["d", "e", "f"], '4':["g", "h", "i"], '5':["j", "k", "l"],'6':["m", "n", "o"], "7":["p", "q", "r","s"], "8": ["t", "u", "v"], "9": ["w","x", "y", "z"]}
        def product(a, b):
            output = []
            for c in a:
                for d in b:
                    output.append(c+d)
            return output

        if len(digits) == 0:
            return []
        elif len(digits) == 1 :
            return hmp[digits]
        else:
            output = product(hmp[digits[0]],  hmp[digits[1]])
            for i in range(2, len(digits)):
                output = product(output, hmp[digits[i]])
            return output




# previous approach
# def cartesian(s1, s2):
#     output = []
#     for i in s1:
#         for j in s2:
#             output.append(i+j)
#
#     return output
#
#
# def letterCombinations(digits: str):
#     graph = {
#         "2": ["a", "b", "c"],
#         "3": ["d", "e", "f"],
#         "4": ["g", "h", "i"],
#         "5": ["j", "k", "l"],
#         "6": ["m", "n", "o"],
#         "7": ["p", "q", "r", "s"],
#         "8": ["t", "u", "v"],
#         "9": ["w", "x", "y", "z"]
#     }
#
#     if len(digits) ==1:
#         return graph[digits]
#     elif len(digits) ==0:
#         return []
#
#     else:
#         temp = cartesian(graph[digits[0]], graph[digits[1]])
#         for i in range(2, len(digits)):
#             temp = cartesian(temp, graph[digits[i]])
#
#     return temp
#
#
# print(letterCombinations("23"))
#
#
#
#
#
#
