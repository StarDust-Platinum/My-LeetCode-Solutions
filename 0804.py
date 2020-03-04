class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
               ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
               "...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for w in words:
            s.add(''.join(morse[ord(c)-97] for c in w))
        return len(s)