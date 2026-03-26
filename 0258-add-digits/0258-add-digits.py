class Solution:
    def addDigits(self, num: int) -> int:
        # ! Base case: if number is already a single digit, return it
        if num < 10:
            return num
        
        # * Initialize sum of digits
        digit_sum = 0
        
        # * Extract and add each digit
        while num > 0:
            digit_sum += num % 10   # add last digit
            num //= 10             # remove last digit
        
        # TODO: Recursively call function until result becomes single digit
        return self.addDigits(digit_sum)