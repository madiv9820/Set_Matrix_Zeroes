## 🛡️ Approach 1: The Safe Simulation (Extra Space)
This approach represents the most intuitive, brute-force way to solve the "Set Matrix Zeroes" problem. It is the perfect starting point for a technical interview before you dive into the crazy $O(1)$ space optimizations.

### 💡 The Intuition
Imagine you are sweeping a minefield. Your job is to find the original bombs (the 0s) and trigger them to obliterate their rows and columns.

**The Problem:** If you find a bomb and immediately turn its row and column into `0`s, how will you know later if the next `0` you see is an original bomb or just the aftermath of your previous explosion? If you aren't careful, the entire grid will collapse into zeroes!

**The Solution:** You need a map! We create an identical $m \times n$ "tracker" grid filled with `False`. Every time our laser beam turns a cell into a `0`, we mark it as `True` on our map. As we sweep the grid, if we see a `0` but our map says it was caused by a laser beam, we safely ignore it.

### 🚶‍♂️ Step-by-Step Logic
1. **Map the Dimensions:** First, grab the number of rows ($m$) and columns ($n$) of the input matrix.
2. **Deploy the Tracker:** Create a new 2D boolean array of the exact same size, initialized entirely to **`False`**. This is our **`visited`** tracker.
3. **Commence the Sweep:** Loop through every single cell **`(r, c)`** in the original matrix from top-left to bottom-right.
4. **Consult the Map:** Before doing anything, check the **`visited`** tracker at **`(r, c)`**. If it is **`True`**, it means this cell was destroyed by a previous laser beam. **Skip it!**
5. **Fire Lasers:** If the cell is **`False`** in the tracker, check its value. If it is an original **`0`**:
    * **Row Laser:** Loop through the entire row **`r`**. Change every cell to **`0`** and mark it as **`True`** in the tracker (unless it was already an original **`0`**).
    * **Column Laser:** Loop through the entire column **`c`**. Change every cell to **`0`** and mark it as **`True`** in the tracker.

### 💻 Pseudocode
```text
FUNCTION set_matrix_zeroes(matrix):
    m = length(matrix)
    n = length(matrix[0])
    
    // Create an identically sized tracker grid
    visited = 2D array of size m x n filled with False
    
    FOR r FROM 0 TO m - 1:
        FOR c FROM 0 TO n - 1:
            
            // Skip if this cell was modified by a previous blast
            IF visited[r][c] is True:
                CONTINUE
                
            // If we found an original bomb, trigger the lasers!
            IF matrix[r][c] == 0:
                
                // 1. Shoot Horizontal Laser
                FOR every cell in row r:
                    IF cell is not original bomb:
                        matrix[row][cell] = 0
                        visited[row][cell] = True
                        
                // 2. Shoot Vertical Laser
                FOR every cell in column c:
                    IF cell is not original bomb:
                        matrix[cell][column] = 0
                        visited[cell][column] = True
```

### 📊 Complexity Analysis
* **⏱️ Time Complexity:** $O(m \times n \times (m + n))$
    * We iterate through every cell in the grid, taking $O(m \times n)$ time.
    * For every single original **`0`** we find, we immediately iterate through its entire row (length $m$) and its entire column (length $n$).
    * In the worst-case scenario (a grid full of zeroes), we do $(m + n)$ extra work for every cell, making this algorithm highly inefficient.

* **💾 Space Complexity:** $O(m \times n)$
    * We allocate a brand-new 2D array (**`visited`**) of size $m \times n$ to keep track of our blasts.
    * While this perfectly protects our original data, it completely fails the strict in-place / $O(1)$ space constraint requested by the problem.
---