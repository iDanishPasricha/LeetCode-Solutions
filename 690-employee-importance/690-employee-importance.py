"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], given_id: int) -> int:
        d={i.id:i for i in employees}
        employee  = d[given_id]
        total_importance = employee.importance
        
        for i in employee.subordinates:
            total_importance+=self.getImportance(employees,i)
        return total_importance
        