class Solution:
    def singleNumber(self, nums: List[int]):
        temp = 0
        for num in nums:
            temp = temp ^ num # XOR
        return temp
