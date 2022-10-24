"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque


class Solution:
    # Employee id to ind Map + BFS (Accepted), O(n) time and space
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_ind = {}
        for i in range(len(employees)):
            iden = employees[i].id
            id_ind[iden] = i

        # BFS on Root Emp
        queue = deque([employees[id_ind[id]]])
        res = 0
        while queue:
            cur = queue.popleft()
            res += cur.importance
            for sub_id in cur.subordinates:
                queue.append(employees[id_ind[sub_id]])
        return res

    # # Employee Map + DFS (Top Voted), O(n) time and space
    # def getImportance(self, employees: List['Employee'], id: int) -> int:
    #     emps = {employee.id: employee for employee in employees}
    #     dfs = lambda id: sum(dfs(sub_id) for sub_id in emps[id].subordinates) + emps[id].importance
    #     return dfs(id)

    # # Employee Map + Readable DFS (Top Voted), O(n) time and space
    # def getImportance(self, employees: List['Employee'], id: int) -> int:
    #     emps = {employee.id: employee for employee in employees}
    #     def dfs(id):
    #         subordinates_importance = sum(dfs(sub_id) for sub_id in emps[id].subordinates)
    #         return subordinates_importance + emps[id].importance
    #     return dfs(id)
