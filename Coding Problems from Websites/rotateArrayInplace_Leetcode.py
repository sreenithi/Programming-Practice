"""
LeetCode - Rotate Array
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == k or len(nums) == 1:
            return
        
        numToReplace = nums[0]
        curIndex = 0
        cycleStart = 0
        
        for i in range(len(nums)):
            
            indToReplace = (curIndex + k) 
            curIndex = indToReplace            
            
            if indToReplace >= len(nums):
                indToReplace %= len(nums)
                curIndex = indToReplace
                if indToReplace == cycleStart:
                    curIndex += 1
                    cycleStart = curIndex
            
            temp = nums[indToReplace]
            nums[indToReplace] = numToReplace
            numToReplace = temp
            
            if indToReplace != curIndex:
                numToReplace = nums[curIndex]

            