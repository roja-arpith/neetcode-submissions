class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        nums_hashmap = Counter(nums)

        sorted_list = sorted(nums_hashmap.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_list[i][0])

        return res
