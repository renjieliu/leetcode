class Solution:
    def validUtf8(self, data: 'List[int]') -> bool: # O( N | N )
        arr = [ bin(_)[2:] for _ in data]
        arr = [ "0" * (8-len(a)) + a for a in arr] #pad 0 to the left , to make it 8 bit long
        #print(arr)
        i = 0
        while i < len(arr): #check each rule, to see if it matches
            curr = arr[i]
            if curr[:5] == "11110":
                if i >= len(arr)-3 or arr[i+1][:2] != "10" or arr[i+2][:2] != "10" or arr[i+3][:2] != "10":
                    return False
                else:
                    i += 4
            elif curr[:4] == "1110":
                if i >= len(arr)-2 or arr[i+1][:2] != "10" or arr[i+2][:2] != "10":
                    return False
                else:
                    i += 3
            elif curr[:3] == "110":
                if i >= len(arr)-1 or arr[i+1][:2] != "10":
                    return False
                else:
                    i += 2
            
            elif curr[:1] == "0":
                i += 1
            
            else: #does not match with any rule.
                return False
            
        return True
    
