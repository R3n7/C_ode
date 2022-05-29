#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
def removeDuplicates(self, nums: List[int]) -> int:
        list1 =[ ]
        list1 = list(set(nums))
        nums.clear()
        for i in list1:
            nums.append(i)
        nums.sort()
        return 
