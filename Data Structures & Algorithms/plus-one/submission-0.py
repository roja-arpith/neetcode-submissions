class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        i = 0
        num = 0

        while i < n:
            num = num * 10 + digits[i]
            i += 1
        
        num = num + 1

        return [int(d) for d in str(num)]