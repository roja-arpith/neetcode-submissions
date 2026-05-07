class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Put all numbers in a set for O(1) lookup
        max_consecutive = 0

        for num in num_set:
            # Only start counting if `num-1` is not in the set
            # This ensures we start from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                consecutive = 1

                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    consecutive += 1

                max_consecutive = max(max_consecutive, consecutive)

        return max_consecutive
