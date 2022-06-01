#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)        
        except:
            count=0
            for i in nums:
                if target>i:
                   count+=1
            return count
