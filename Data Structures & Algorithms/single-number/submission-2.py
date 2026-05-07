class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashmap = Counter(nums)

        # for i in range(len(nums)):
        #     if hashmap[nums[i]] == 1:
        #         return nums[i]
        
        # return -1

        # res = 0

        # for i in nums:
        #     res ^= i
        
        # return res

        seen = set()
        res = 0

        for i in nums:
            if i not in seen:
                res += i
                seen.add(i)
            else:
                res -= i
            
        return res