class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for index, number in enumerate(nums):
            complement = target - number 
            if complement not in D:
                D[number] = index
            else:
                return [D[complement], index]
