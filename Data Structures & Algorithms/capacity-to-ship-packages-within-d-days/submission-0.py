class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)
        ans = 0

        while l <= r:
            mid = l + (r - l) // 2

            day = 1
            current_load = 0
            for i in weights:
                if current_load + i > mid:
                    day += 1
                    current_load = 0
                current_load += i
            
            if day <= days:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
        

                