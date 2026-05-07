class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = set(nums)
        x = []
        for i in l:
            c = nums.count(i)
            x.append([c,i])
        x.sort()
        res = []
        while len(res) < k:
            res.append(x.pop()[1])
        return res
                
                
        