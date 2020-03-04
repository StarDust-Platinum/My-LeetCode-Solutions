class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
		chars = [ch.lower() for ch in licensePlate if ch.isalpha()]
		chars = ''.join(chars)
		words.sort(key=len)
		for word in words:
			temp = chars
			for char in word:
				temp = temp.replace(char, '', 1)
				if len(temp) == 0:
					return word