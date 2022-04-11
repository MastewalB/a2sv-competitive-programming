"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def calcTotalSubordinates(employee):
            total = 0
            total += employee.importance
            for sub in employee.subordinates:
                total += calcTotalSubordinates(findEmployee(sub))
            return total

        def findEmployee(emp_id):
            for i in employees:
                if i.id == emp_id:
                    return i

        emp = findEmployee(id)
        return calcTotalSubordinates(emp)
