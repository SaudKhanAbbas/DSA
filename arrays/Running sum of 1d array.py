class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0 
        result = []
        for num in nums:
            runningSum = runningSum + num
            result.append(runningSum)
        
        return result
