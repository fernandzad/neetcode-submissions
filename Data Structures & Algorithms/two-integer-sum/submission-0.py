class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = dict()
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if previous_map.get(difference) is None:
                previous_map[nums[i]] = i
            else:
                return [previous_map.get(difference), i]
            