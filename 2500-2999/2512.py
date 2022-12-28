class Solution:
    def topStudents(self, positive_feedback: 'List[str]', negative_feedback: 'List[str]', report: 'List[str]', student_id: 'List[int]', k: int) -> 'List[int]': # O( NlogN | N )
        p = set(positive_feedback) # turn the words to set, to speed up the lookup
        n = set(negative_feedback)
        score = []
        for i in range(len(report)): #calculate the score for each student
            arr = report[i].split(' ') 
            score = 0 
            for a in arr:
                if a in p:
                    score += 3 
                elif a in n:
                    score -= 1
            student_id[i] = [student_id[i], score]
        
        student_id.sort(key = lambda x: x[0]) # sort by ID
        student_id.sort(key = lambda x: x[1], reverse = True)  #sort by score
        output = []
        for i in range(k): # get the first k student
            output.append(student_id[i][0])
        
        return output
    
    
