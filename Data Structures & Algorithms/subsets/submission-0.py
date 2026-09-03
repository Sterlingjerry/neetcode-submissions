class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
    
        def backtrack(i):
            # base case
            if i == len(nums):
                return result.append(subset.copy())

            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)

        backtrack(0)

        return result