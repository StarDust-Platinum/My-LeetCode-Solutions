class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        cur = []
        i = 0
        for x in pushed:
            cur.append(x)
            while cur and cur[-1] == popped[i]:
                i += 1
                cur.pop()
        return i == len(popped)