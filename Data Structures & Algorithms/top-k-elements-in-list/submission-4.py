class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt,num])
        
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        
        # return res

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]

        # # Count frequency
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)

        # # Place numbers into buckets
        # for n, c in count.items():
        #     freq[c].append(n)

        # res = []

        # # Traverse from highest frequency
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)

        #         if len(res) == k:
        #             return res


        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(
            freq,
            key=lambda x: freq[x],
            reverse=True
        )

        return sorted_nums[:k]