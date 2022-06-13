import math
class Solution:
    def mySqrt(self, x: int) -> int:
        return math.gcd(x,int(x**0.5)) if x**0.5 == 1 else int(x**0.5)
