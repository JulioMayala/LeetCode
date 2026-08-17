class Solution(object):
    def isPalindrome(self, x):
        cadena=str(x)
        return cadena== cadena[::-1]