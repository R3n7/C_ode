class Solution:
    def climbStairs(self, n: int) -> int:
        list1 = {}
        list1[0]=0
        list1[1]=1
        list1[2]=2
        for i in range(3,n+1):
            list1[i] = list1[i-1]+list1[i-2]
        #print(list1)
        return list1[n]
