#https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list1 =[ ]
        list1.extend(nums1)
        list1.extend(nums2)
        list1.sort()
        if (len(nums1)+len(nums2))%2==0:
            #print(list1[(len(nums1)+len(nums2))//2],list1[(len(nums1)+len(nums2))//2 -1])
            return (list1[(len(nums1)+len(nums2))//2]+list1[(len(nums1)+len(nums2))//2 -1])/2
        return list1[(len(nums1)+len(nums2))//2]
