class Solution:

    def findCommonPrefix(self, str1, str2):
        output = ""
        cnt = len(str1) if len(str1) < len(str2) else len(str2)
        for i in range(0,cnt):
            if str1[i] == str2[i]:
                output+=str1[i]
            else:
                break
        return output



    def longestCommonPrefix(self, strs):
        # lenMost = len(common)
        if len(strs)<2:
            return ""
        else:
            current = self.findCommonPrefix(strs[0],strs[1])
            for i in range(2, len(strs)):
                current = self.findCommonPrefix(current,strs[i])
        return current


input = list()
input = "ab abc abdc".split(" ")
#print(input)
print(Solution.longestCommonPrefix(input))