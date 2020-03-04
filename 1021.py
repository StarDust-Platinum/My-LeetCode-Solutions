class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        r = ""
        left = 0
        right = 0
        j = 0
        for i in range(len(S)):
            if S[i]=="(":
                left += 1
            else:
                right += 1
            if left == right:
                r += S[j+1:i]
                j = i + 1
        return r