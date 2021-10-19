class Solution:
    def countStudents(self, students: 'List[int]', sandwiches: 'List[int]') -> int:
        while students:
            if students[0] != sandwiches[0]:
                x = sum(students)
                if x == len(students) or x == 0:  # all 1 or all 0 , no need to continue
                    return len(students)
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
        return 0

