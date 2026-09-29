class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        result = False
        for i in nums:
            if i in hash_set:
                result = True
                break
            hash_set.add(i)
        return result

        