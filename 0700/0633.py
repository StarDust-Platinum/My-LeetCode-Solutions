class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = set()
        count = int(math.sqrt(c))
        for i in range(count + 1):
            sq.add(i ** 2)

        for n in sq:
            if c - n in sq:
                return True

        return False