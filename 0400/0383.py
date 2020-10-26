class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        R = collections.Counter(ransomNote)
        M = collections.Counter(magazine)
        for key in R.keys():
            if key not in M.keys() or R[key]>M[key]:
                return False
        return True