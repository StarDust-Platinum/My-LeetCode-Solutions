class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        x = str.split(' ')
        lsp = len(set(pattern))
        lsx = len(set(x))
        return len(x)==len(pattern) and lsx==lsp and lsp== len(set(zip(pattern, x)))