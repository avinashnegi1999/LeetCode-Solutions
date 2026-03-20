from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}  # remember numbers
        
        for i in range(len(nums)):
            number = nums[i]
            
            need = target - number  # what we need
            
            if need in bag:  # if already seen
                return [bag[need], i]
            
            bag[number] = i  # remember this number