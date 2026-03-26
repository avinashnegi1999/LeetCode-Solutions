class Solution:
    def addDigits(self, num: int) -> int:
        # ! Edge case: if number is 0, result is 0 (digital root rule)
        if num == 0:
            return 0
        
        # * Use Digital Root formula:
        # * Repeated sum of digits follows a pattern in modulo 9
        # * This avoids loops/recursion and runs in O(1)
        # * Formula: 1 + (num - 1) % 9
        return 1 + (num - 1) % 9