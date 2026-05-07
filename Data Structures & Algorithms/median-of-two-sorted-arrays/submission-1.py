class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()

        length = len(nums) - 1

        if length % 2 == 0:
            return nums[length//2]
        else:
            return (nums[length//2] + nums[(length+1)//2] )/ 2
        
