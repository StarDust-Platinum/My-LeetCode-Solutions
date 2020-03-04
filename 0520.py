class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word[1:] == word[1:].lower():
            return True
        else:
            return False
        