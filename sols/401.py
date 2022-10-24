class Solution:
    # # Backtracking (Accepted), O(1) time and space from problem constraint
    # def readBinaryWatch(self, turnedOn: int) -> List[str]:
    #     def get_pos(num_on, arr, limit):
    #         if num_on == 0:
    #             return [0]
    #         elif num_on == 1:
    #             return arr

    #         res = []
    #         diff = len(arr) - num_on
    #         for i in range(diff + 1):
    #             l = get_pos(num_on-1, arr[i+1:], limit)
    #             for elem in range(len(l)):
    #                 if l[elem] + arr[i] <= limit:
    #                     res.append(l[elem] + arr[i])
    #         return res

    #     H = [8, 4, 2, 1]
    #     M = [32, 16, 8, 4, 2, 1]

    #     res = []

    #     for i in range(min(turnedOn, 4) + 1):
    #         on_hrs = i
    #         on_mins = turnedOn - i
    #         pos_hours = get_pos(on_hrs, H, 11)
    #         pos_mins = get_pos(on_mins, M, 59)
    #         for h in pos_hours:
    #             for m in pos_mins:
    #                 res.append(str(h) + ':' + (str(m) if m > 9 else  '0' + str(m)))

    #     return res

    # # DFS (Top Voted), O(1) time and space
    # def readBinaryWatch(self, n):

    #     def dfs(n, hours, mins, idx):
    #         if hours >= 12 or mins > 59: return
    #         if not n:
    #             res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
    #             return
    #         for i in range(idx, 10):
    #             if i < 4:
    #                 dfs(n - 1, hours | (1 << i), mins, i + 1)
    #             else:
    #                 k = i - 4
    #                 dfs(n - 1, hours, mins | (1 << k), i + 1)

    #     res = []
    #     dfs(n, 0, 0, 0)
    #     return res

    # Collect the One Bits, List Comprehension (Top Voted), O(1) time and space
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == turnedOn]
