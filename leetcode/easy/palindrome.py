# Input: x = 121
# Output: true

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        b = 0
        c = x
        while c:
            b = 10 * b + c % 10
            c //= 10 #python3 uses // for division
        return b == x 
