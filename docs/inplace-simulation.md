## 🐢 Approach 2: The In-Place Marker (O(1) Space)
This approach is the perfect stepping stone during an interview. It proves to the interviewer that you understand how to solve the O(1) space constraint, even if the time complexity isn't fully optimized yet.

### 💡 The Intuition
In Approach 1, we used a massive second grid just to remember which zeroes were "original bombs" and which zeroes were the "aftermath" of our laser beams.

**The Trick:** What if we just used a different type of blast?
Instead of instantly destroying a cell by turning it into a **`0`**, we can temporarily blast it with a completely different data type—like **`None`** (or a number safely outside the constraint bounds).

By doing this, any original **`0s`** in the grid stay perfectly intact as **`0s`**. As we sweep the grid, we only trigger laser beams when we see a true **`0`**, and we safely ignore any **`None`** markers. Once the dust settles, we do one final sweep to convert all the **`None`** markers into **`0s`**.

### 🚶‍♂️ Step-by-Step Logic
1. **Map the Dimensions:** Grab the number of rows (**`m`**) and columns (**`n`**) of the input matrix.

2. **First Pass (The Sweep):** Loop through every single cell **`(r, c)`** in the matrix.

3. **Fire Temporary Lasers:** If the current cell is exactly **`0`**:
    * **Row Laser:** Loop through the entire row **`r`**. If a cell is NOT already a **`0`**, change it to **`None`**.
    * **Column Laser:** Loop through the entire column **`c`**. If a cell is NOT already a **`0`**, change it to **`None`**.
    * *(Note: We deliberately skip overwriting other **`0s`** so they can trigger their own blasts when we reach them!)*

4. **Second Pass (The Cleanup):** Now that the entire board is filled with original **`0s`** and our temporary **`None`** blasts, loop through the grid one more time.

5. **Finalize the Destruction:** Whenever you see a **`None`**, change it to a **`0`**.

### 💻 Pseudocode
```text
FUNCTION set_matrix_zeroes(matrix):
    m = length(matrix)
    n = length(matrix[0])
    
    // PASS 1: Find bombs and mark blast radii with 'None'
    FOR r FROM 0 TO m - 1:
        FOR c FROM 0 TO n - 1:
            
            // If we find an original bomb
            IF matrix[r][c] == 0:
                
                // 1. Shoot Horizontal 'None' Laser
                FOR every cell in row r:
                    IF cell is NOT 0:
                        matrix[row][cell] = None
                        
                // 2. Shoot Vertical 'None' Laser
                FOR every cell in column c:
                    IF cell is NOT 0:
                        matrix[cell][column] = None
                        
    // PASS 2: Convert all 'None' markers to real 0s
    FOR r FROM 0 TO m - 1:
        FOR c FROM 0 TO n - 1:
            IF matrix[r][c] == None:
                matrix[r][c] = 0
```

### 📊 Complexity Analysis
* **⏱️ Time Complexity:** $O(m \times n \times (m + n))$
    * We iterate through the grid, which takes $O(m \times n)$ time.
    * For every single original **`0`** we find, we immediately iterate through its entire row (length $m$) and column (length $n$).
    * Just like Approach 1, if the grid has a ton of zeroes, we end up overwriting the exact same cells with **`None`** hundreds of times. It works, but it's slow!

* **💾 Space Complexity:** $O(1)$
    * We did it! We completely eliminated the extra **`visited`** array.
    * Because we strictly modified the matrix in-place and only used a temporary data type (**`None`**) that requires no scaling memory allocation, our space complexity is perfectly constant.
---