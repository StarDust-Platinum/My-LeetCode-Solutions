class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(A, p, r):
            x = A[r]
            i = p - 1
            for j in range(p, r):
                if A[j] <= x:
                    i = i + 1
                    A[i], A[j] = A[j], A[i]
            A[i+1], A[r] = A[r], A[i+1]
            return i+1

        def randomized_partition(A, p, r):
            i = random.randrange(0, r+1)
            A[r], A[i] = A[i], A[r]
            return partition(A, p, r)

        def sort(A, p, r):
            if p < r:
                q = partition(A, p, r)
                sort(A, p, q-1)
                sort(A, q+1, r)

        N = len(nums)
        sort(nums, 0, N-1)
        return nums