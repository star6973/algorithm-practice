class Solution(object):
    def threeSum(self, nums):
        for i in range(len(nums)):
            print(nums[i])
            for j in range(i+1, len(nums)-1):
                # if nums[i] + nums[j] + nums[j+1] == 0:
                print(nums[j], nums[j+1])
        
nums = [-2,0,1,1,2]
sol = Solution()
sol.threeSum(nums)