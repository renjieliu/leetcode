"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        for emp in employees:
            if emp.id == id:
                if len(emp.subordinates) == 0:
                    return emp.importance
                else:
                    sum_importance = emp.importance
                    for s in emp.subordinates:
                        sum_importance += self.getImportance(employees, s)

        return sum_importance


e = [Employee]
e.append(Employee(1, 5, [2, 3]))
e.append(Employee(2, 3, []))
e.append(Employee(3, 3, []))
print(Solution.getImportance(e, 1))
