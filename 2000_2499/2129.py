class Solution:
    def capitalizeTitle(self, title: str) -> str: #one pass
        def helper(curr):
            if len(curr) > 2:
                return curr[0].upper()+ curr[1:].lower() 
            else:
                return curr.lower()  
        output = ""
        curr = ""
        for t in title:
            if t == " ":
                output += helper(curr) + " "
                curr = ""
            else:
                curr += t
        output += helper(curr)
        return output
    


# class Solution:
#     def capitalizeTitle(self, title: str) -> str: #break and join
#         arr = title.split(' ')
#         for i in range(len(arr)):
#             curr = arr[i]
#             if len(curr) <= 2:
#                 arr[i] = arr[i].lower()
#             else:
#                 arr[i] = arr[i][0].upper() + arr[i][1:].lower()
#         return ' '.join(arr)
    

    