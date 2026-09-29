class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {} # value : index
        for i in range(0, len(nums)):
            difference = target - nums[i] # calculate the difference
            if previous_map.get(difference) is None: # we check if the value already exists in the dictionary
                previous_map[nums[i]] = i # if not, we store it
            else: # if it exists it means we found the solution
                return [previous_map.get(difference), i]
            