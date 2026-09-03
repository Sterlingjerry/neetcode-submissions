class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result =[]   
        current =[]
        def backtrack(i, total):
            if total == target:
                result.append(current.copy())
                return

            if total > target or i == len(nums):
                return

            current.append(nums[i])

            backtrack(i, total + nums[i])

            current.pop()

            backtrack(i + 1, total)
        
        backtrack(0,0)
        return result

        