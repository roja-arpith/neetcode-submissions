class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = 0
        # j = len(nums) - 1

        # while i < j:
        #     if nums[i] + nums[j] == target:
        #         return [i,j]
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     else:
        #         j -= 1
        
        # return []

        hashmap = {}
        seen = set()

        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                return [hashmap[num], i]
                
            hashmap[nums[i]] = i
        
