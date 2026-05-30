"""
================================================================================
📄 File: approaches.py
================================================================================
Description: 
    Solutions for "Set Matrix Zeroes" (LeetCode 73).
    When a 0 is found, its entire row and column must be obliterated (set to 0).

Approaches Included:
    1. _approach_01_simulation_with_extra_space -> The Safe Way O(m*n) space 🛡️
    2. _approach_02_inplace_simulation          -> The None-Marker Trick O(1) space, but slower 🐢
    3. _approach_03_optimal_inplace             -> The FAANG "Notice Board" Trick O(1) space & O(m*n) time 🚀
================================================================================
"""
from typing import List

class Approaches:
    # 🎯 HELPER 1: Shoot a vertical laser (Iterates through rows for a fixed column)
    def __set_row(
        self, 
        row: int, 
        column: int, 
        visited: List[List[bool]] = None, 
        value: int = 0
    ) -> None:
        for r in range(self.__m):
            # Skip if it's the blast origin, already a 0, or already visited
            if (
                r == row or 
                self._matrix[r][column] == 0 or 
                (visited and visited[r][column])
            ):
                continue
            else:
                self._matrix[r][column] = value
                if visited: visited[r][column] = True

    # 🎯 HELPER 2: Shoot a horizontal laser (Iterates through columns for a fixed row)
    def __set_column(
        self, 
        row: int, 
        column: int, 
        visited: List[List[bool]] = None, 
        value: int = 0
    ) -> None:
        for c in range(self.__n):
            # Skip if it's the blast origin, already a 0, or already visited
            if (
                c == column or
                self._matrix[row][c] == 0 or
                (visited and visited[row][c])
            ):
                continue
            else:
                self._matrix[row][c] = value
                if visited: visited[row][c] = True

    def _approach_01_simulation_with_extra_space(self) -> None:
        # 🛡️ APPROACH 1: The Safe Simulation
        # We use an identical boolean matrix to track where we've already dropped bombs.
        # Space: O(m*n) | Time: O(m*n*(m+n))
        
        self.__m: int = len(self._matrix)
        self.__n: int = len(self._matrix[0])

        # 📝 Create our O(m*n) visited tracker
        self.__visited: List[List[bool]] = [[False] * self.__n for _ in range(self.__m)]

        for r in range(self.__m):
            for c in range(self.__n):
                if self.__visited[r][c]: 
                    continue
                elif self._matrix[r][c] == 0:
                    # 💥 Found an original 0! Trigger the lasers.
                    self.__set_row(row = r, column = c, visited = self.__visited)
                    self.__set_column(row = r, column = c, visited = self.__visited)

    def _approach_02_inplace_simulation(self) -> None:
        # 🐢 APPROACH 2: The In-Place Marker
        # Uses `None` as a temporary marker so we don't need a visited matrix!
        # Space: O(1) | Time: O(m*n*(m+n))
        
        self.__m: int = len(self._matrix)
        self.__n: int = len(self._matrix[0])

        # 🔍 Pass 1: Find 0s and mark their blast radii with `None`
        for r in range(self.__m):
            for c in range(self.__n):
                if self._matrix[r][c] == 0:
                    self.__set_row(row = r, column = c, value = None)
                    self.__set_column(row = r, column = c, value = None)
        
        # 💥 Pass 2: Convert all temporary `None` markers into final `0`s
        for r in range(self.__m):
            for c in range(self.__n):
                if self._matrix[r][c] == None:
                    self._matrix[r][c] = 0
    
    def _approach_03_optimal_inplace(self) -> None:
        # 🚀 APPROACH 3: The Notice Board Trick
        # Uses the first row and first column of the matrix itself to take notes!
        # Space: O(1) | Time: O(m*n) -> FAANG Optimal!
        
        self.__m: int = len(self._matrix)
        self.__n: int = len(self._matrix[0])

        # 🕵️ STEP 1: Check the Notice Boards before we overwrite them!
        # 💡 Note: `self._matrix[r][0]` loops through rows on col 0 (First Column)
        # 💡 Note: `self._matrix[0][c]` loops through cols on row 0 (First Row)
        first_row_zero: bool = any(self._matrix[r][0] == 0 for r in range(self.__m))
        first_col_zero: bool = any(self._matrix[0][c] == 0 for c in range(self.__n))

        # 📝 STEP 2: Find inner 0s and write them to the Notice Boards
        for r in range(1, self.__m):
            for c in range(1, self.__n):
                if self._matrix[r][c] == 0:
                    self._matrix[r][0] = 0  # Mark the row's notice board
                    self._matrix[0][c] = 0  # Mark the column's notice board
        
        # 💥 STEP 3: Read the Notice Boards and obliterate the inner rooms
        for r in range(1, self.__m):
            for c in range(1, self.__n):
                if self._matrix[r][0] == 0 or self._matrix[0][c] == 0:
                    self._matrix[r][c] = 0
        
        # 🧹 STEP 4: Finally, clean up the Notice Boards themselves!
        if first_row_zero:
            for r in range(self.__m):
                self._matrix[r][0] = 0
        
        if first_col_zero:
            for c in range(self.__n):
                self._matrix[0][c] = 0
