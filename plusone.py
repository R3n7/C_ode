#https://leetcode.com/problems/plus-one/submissions/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(x) for x in digits])
        num = int(num)
        num+=1
        return [int(x) for x in str(num)]
