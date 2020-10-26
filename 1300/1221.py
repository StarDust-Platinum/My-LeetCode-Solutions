class Solution:
    def balancedStringSplit(self, s: str) -> int:
        status = [0, 0]
        count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                status[0] += 1
            else:
                status[1] += 1
            if status[0] == status[1]:
                count += 1
        return count