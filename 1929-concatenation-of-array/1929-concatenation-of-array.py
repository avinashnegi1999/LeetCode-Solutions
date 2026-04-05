class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # * Concatenate array with itself
        # ! Creates a new list of size 2n
        # ? Why works: nums + nums duplicates elements in order
        # TODO: Optimize only if memory constraints are strict
        return nums + nums