class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        dict_r = {} 
        dict_c = {}
        for i in indices:
            if i[0] not in dict_r:
                dict_r[i[0]] = 0
            dict_r[i[0]] += 1
            
            if i[1] not in dict_c:
                dict_c[i[1]] = 0
            dict_c[i[1]] += 1
        
        c_odd = 0 
        c_even= 0
        for k, v in dict_c.items():
            if v%2 ==0:
                c_even +=1
            else:
                c_odd += 1
        
        output = 0
        for i in range(n):
            if i not in dict_r:
                output += c_odd
            else: 
                if dict_r[i] %2 ==0:
                    output+= c_odd
                    
                else:
                    curr = m - c_odd 
                    output+= curr
        return output