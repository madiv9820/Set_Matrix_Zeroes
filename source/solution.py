"""
================================================================================
📄 File: solution.py
================================================================================
Description: 
    The main entry point and runner for "Set Matrix Zeroes" (LeetCode 73).
    This file serves as the clean interface expected by the caller (or LeetCode),
    delegating all the heavy algorithmic lifting to the Approaches class! 🏋️‍♂️

Usage:
    Instantiate the Solution class and call `setZeroes(matrix)`.
    You can easily test different time/space complexities by commenting 
    and uncommenting the approach methods inside! 🧪
================================================================================
"""
from typing import List
from approaches import Approaches

class Solution(Approaches):
    # 🧩 By inheriting from Approaches, this class automatically gains access 
    # to all the explosive laser-beam algorithms we built in `approaches.py`!
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Calculates the blast radii of all 0s in the grid.
        Do not return anything, modify the matrix in-place instead.
        """
        
        # 📦 Bind the input matrix to our instance state so the hidden 
        # approach methods can seamlessly access and mutate it.
        self._matrix = matrix
        
        # 🚀 EXECUTION BLOCK
        # Choose your weapon! Comment/uncomment to swap the active algorithm.
        
        # self._approach_01_simulation_with_extra_space()  # 🛡️ Safe, O(m*n) space
        # self._approach_02_inplace_simulation()           # 🐢 None-marker trick, O(1) space
        self._approach_03_optimal_inplace()                # 🧠 The FAANG Notice Board trick, O(1) space