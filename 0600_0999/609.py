class Solution:
    def findDuplicate(self, paths: 'List[str]') -> 'List[List[str]]': # O( N*p | N ) P is the longest length of the path
        files = defaultdict(lambda : [])
        for p in paths:
            arr = p.split(' ') # split to folder, files
            path = arr[0]
            for f in arr[1:]: # go through files
                file, content = f.split('(')
                c = content[:-1] # take out the last ")"
                files[c].append(path + '/' + file)
        return [v for k,v in files.items() if len(v)> 1 ]
    




# previous solution

# class Solution:
#     def findDuplicate(self, paths: 'List[str]') -> 'List[List[str]]':
#         hmp = {} #using a hashmap to store content as key, and array of the file path as value
#         for p in paths:
#             arr = p.split(' ')
#             d = arr[0]
#             for file in arr[1:]: # input: "root/a 1.txt(abcd) 2.txt(efgh)"
#                 stk = file.split('(')
#                 file = d+"/" + stk[0]
#                 content = stk[1][:-1]
#                 if content not in hmp:
#                     hmp[content] = []
#                 hmp[content].append(file)
#         output = []
#         for k, v in hmp.items():
#             if len(v) > 1:
#                 output.append(v)
#         return output

# previous approach
# def findDuplicate(paths: 'List[str]'):
#     map = {}
#     output = []
#
#     for i in paths:
#         folder = i.split(" ")[0] + "/"
#         files = i.split(" ")[1:]
#         for j in files:
#             content = j.split("(")[1].replace(")","")
#             fileName = j.split("(")[0]
#             fullpath  = folder  + fileName
#             if content not in map:
#                 map[content] =[]
#             map[content].append(fullpath)
#
#     for k,v in map.items():
#         if len(v) >1:
#             temp = []
#             for x in v:
#                 temp.append(x)
#
#             output.append(temp)
#
#     return output
#
# print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
# print(findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(esfgh)"]))
