class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)

        for i in range(len(nums)):
            if hashmap[nums[i]] == 1:
                return nums[i]
        
        return -1