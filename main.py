from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    num_map = {}

    for i in range(len(nums)):

        complement = target - nums[i]

        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i
