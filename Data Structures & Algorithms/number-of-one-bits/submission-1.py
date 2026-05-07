class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # n = bin(n)
        # count = 0

        # for i in n:
        #     if i == "1":
        #         count += 1
        
        # return count

        count = 0

        while n:
            count += n & 1
            n = n >> 1
        
        return count