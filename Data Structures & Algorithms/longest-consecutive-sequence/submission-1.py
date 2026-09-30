class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We need to check for initial values
        # An initial value is a number n where n - 1 is not in the list
        hash_set = set(nums)
        longest = 0
        for n in nums:
            initial = n - 1
            if initial not in hash_set:
                length = 1
                while (n + length) in hash_set:
                    length += 1
                longest = max(longest, length)
        return longest
        