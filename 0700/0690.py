"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ti = [0]
        
        def dfs(x):
            ti[0] = ti[0] + x.importance
            for employee in employees:
                if employee.id in x.subordinates:
                    dfs(employee)        
        
        for employee in employees:
            if employee.id == id:
                dfs(employee)
        return ti[0]