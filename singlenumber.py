class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=0
            hashmap[nums[i]]+=1
        for i in hashmap.keys():
            if hashmap[i]==1:
                return i
