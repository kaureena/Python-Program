from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Handle empty list case
            return 0

        i = 0  # Pointer for unique elements

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1



nums = [1, 1, 2]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k, nums[:k])