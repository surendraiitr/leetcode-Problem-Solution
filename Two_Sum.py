class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = []
        for i in nums:
            c.append(i)
        nums.sort()
        i  = 0
        l = []
        f = []
        j = len(nums) - 1
        while(1):
            if nums[i] + nums[j] == target:
                #print(nums[i], nums[j])
                l.append(nums[i])
                l.append(nums[j])
                break
            elif nums[i] + nums[j] > target:
                j-=1
            else :
                i+=1
        for i in range(len(c)):
            if c[i] in l:
                f.append(i)
        return f      
