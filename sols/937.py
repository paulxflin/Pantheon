class Solution:
    # Index and tuple key (Accepted), O(n log n) time, O(n) space
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []
        for log in logs:
            i = log.index(' ')
            if log[i+1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def make_tup(s):
            i = s.index(' ')
            return (s[i+1:], s[:i])
        letter_logs.sort(key=make_tup)
        return letter_logs + digit_logs

    # Split and lambdas (Top Voted), O(n log n) time, O(n) space
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # when suffix is tie, sort by identifier
        letters.sort(key=lambda x: x.split()[0])
        letters.sort(key=lambda x: x.split()[1:])  # sort by suffix
        result = letters + digits  # put digit logs after letter logs
        return result
