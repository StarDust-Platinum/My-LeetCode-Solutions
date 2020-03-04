class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        h = heights.copy()
        h.sort()
        for i in range(len(heights)):
            if heights[i] != h[i]:
                count += 1
        return count