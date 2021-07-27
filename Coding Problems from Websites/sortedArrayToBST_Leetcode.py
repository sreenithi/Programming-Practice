"""
LeetCode Question - Convert Sorted Array to Binary Search Tree
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3827/

Question:
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.__sortedArrayToBST(nums, 0, len(nums))
    
    def __sortedArrayToBST(self, nums, start, end):
        
        if start == end:
            return None
        
        if (end - start) == 1:
            return TreeNode(nums[start])
        
        midIndex = (start + end) // 2
        root = TreeNode(nums[midIndex])
        
        leftTree = self.__sortedArrayToBST(nums, start, midIndex)
        rightTree = self.__sortedArrayToBST(nums, midIndex+1, end)
        
        root.left = leftTree
        root.right = rightTree
        
        return root