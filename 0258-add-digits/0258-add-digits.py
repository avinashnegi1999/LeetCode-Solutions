class Solution:
    def addDigits(self, num: int) -> int:
        # ! Edge case: if number is 0, answer is 0
        if num == 0:
            return 0
        
        # * O(1) trick using modulo 9 (observed pattern in digit sums)
        return 1 + (num - 1) % 9


# ------------------- My Recursive Approach -------------------

# class Solution:
#     def addDigits(self, num: int) -> int:
#         # ! if single digit, just return it
#         if num < 10:
#             return num
#
#         # * sum all digits manually
#         digit_sum = 0
#         while num > 0:
#             digit_sum += num % 10
#             num //= 10
#
#         # * keep repeating until one digit left
#         return self.addDigits(digit_sum)
#
# * example:
# * 38 -> 3+8 = 11
# * 11 -> 1+1 = 2
# * answer = 2