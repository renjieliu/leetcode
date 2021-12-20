class Solution:
    def addSpaces(self, s: str, spaces: 'List[int]') -> str:
        if spaces == []:
            return s
        else:
            output = ""
            ptr = 0 #the pointer in the spaces array
            for i, c in enumerate(s):
                if i == spaces[ptr]:
                    output += " " + c #add a space here and add the c
                    if ptr < len(spaces)-1:
                        ptr+=1
                    else:
                        return output + s[i+1:]
                else:
                    output += c
            return output


        
