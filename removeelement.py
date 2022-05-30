#https://leetcode.com/problems/remove-element/submissions/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=[i for i in range(len(nums)) if nums[i]==val]
        for k in range(len(l)):
            nums.remove(val)
        return
