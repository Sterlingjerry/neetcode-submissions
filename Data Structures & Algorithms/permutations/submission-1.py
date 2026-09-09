class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num not in current:
                    current.append(num)  # choose
                    backtrack()          # explore
                    current.pop()

        backtrack()
        return result
        