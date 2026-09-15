class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}
        for i in range(len(nums)):
            if nums[i] in num_counts:
                num_counts[nums[i]] += 1
            else:
                num_counts[nums[i]] = 1
        
        for key in num_counts:
            if num_counts[key] > 1:
                return True
        return False