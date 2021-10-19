class Solution:
    def reverseWords(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(arr, a, b): # reverse arr, range [a,b)
            t = arr[a:b][::-1]
            for j in range(a, b):
                arr[j] = t[j-a] #t is the new arr, start at 0, need to do j-a to get the correct index in t

        rev(s, 0, len(s))
        prevSpace = -1
        i = 0
        while i < len(s):
            if s[i] == " ":
                rev(s, prevSpace+1, i)
                prevSpace = i
            i+=1
        rev(s, prevSpace+1, len(s)) # reverse the last word



# previous approach
# class Solution:
#     def reverseWords(self, s: 'List[str]') -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         def reverse(s,l,r):  #reverse from l to r
#             for i in range(l, l+(r-l)//2+1): #only need to iterate the first half, current right is (i-l)
#                 s[i], s[r-(i-l)] = s[r-(i-l)], s[i]
#                 #print(s[i],s[r-(i-l)], s )
#
#         reverse(s, 0, len(s)-1 )
#         curr = 0
#         for i in range(len(s)):
#             if s[i] == " ":
#                 reverse(s, curr, i-1)
#                 curr = i+1
#         reverse(s,curr, len(s)-1) # reverse the last part
