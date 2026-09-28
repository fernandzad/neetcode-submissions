class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = {}
        for nu in nums:
            bucket[str(nu)] = bucket.get(str(nu), 0) + 1
        # for i in range(1, 4):
        #     print(f"{i}: {bucket[str(i)]}")

        hasDuplicates = False
        for (_, val) in bucket.items():
            if val > 1:
                hasDuplicates = True
                return hasDuplicates
        return hasDuplicates