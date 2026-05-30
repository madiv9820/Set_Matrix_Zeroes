## 🚀 Approach 3: The FAANG Optimal (The Notice Board Trick)
This is it. The holy grail of the "Set Matrix Zeroes" problem. It achieves perfect $O(1)$ space without sacrificing our $O(m \times n)$ time complexity. If you pull this off in a technical interview, you are signaling to the interviewer that you understand advanced memory manipulation.

### 🧠 The Intuition
In Approach 1, we used a massive extra grid to keep track of our blasts. In Approach 2, we did duplicate work by firing lasers every time we saw a zero.

**The Brilliant Trick:** What if the matrix itself could keep track of the notes?
We can hijack the **First Row** and **First Column** of the grid and use them as our "Notice Boards".

When we sweep through the inner rooms of the grid and find a **`0`**, we don't blow anything up immediately. Instead, we just walk over to that row's left edge and write a **`0`**. Then we walk up to that column's top edge and write a **`0`**.

Once we finish taking notes, we simply read the Notice Boards. If a row or column is marked for destruction, we obliterate the inner cells.

**⚠️ The Catch (The `[0][0]` Overlap):**  The very first cell **`matrix[0][0]`** belongs to BOTH the first row and the first column! If we overwrite it, we won't know which one it was meant for. <br> **The Fix:** Before we write anything on the Notice Boards, we scan them to see if they originally had any zeroes natively. We save those answers in two simple boolean variables (**`first_row_zero`** and **`first_col_zero`**).

### 🚶‍♂️ Step-by-Step Logic
1. **🕵️ Step 1: Inspect the Notice Boards** <br>
Scan the first row and the first column. If there is a **`0`** anywhere in the first row, set **`first_row_zero = True`**. If there is a **`0`** in the first column, set **`first_col_zero = True`**. Do this before making any changes to the board!

2. **📝 Step 2: Take Notes** <br>
Loop through the **inner** matrix (starting from index **`1`** for both rows and columns). If you find a **`0`** at (r, c), mark its row's notice board **`matrix[r][0] = 0`** and its column's notice board **`matrix[0][c] = 0`**.

3. **💥 Step 3: Trigger the Blasts** <br>
Loop through the **inner** matrix one more time. For every cell **`(r, c)`**, check its row's notice board and its column's notice board. If *either* of them is a **`0`**, set the current cell **`matrix[r][c] = 0`**.

4. **🧹 Step 4: Destroy the Notice Boards** <br>
Now that the inner matrix is handled, look at your two boolean variables from Step 1. If **`first_row_zero`** is **`True`**, turn the entire first row to **`0s`**. If **`first_col_zero`** is **`True`**, turn the entire first column to **`0s`**.

### 💻 Pseudocode
```text
FUNCTION set_matrix_zeroes(matrix):
    m = length(matrix)
    n = length(matrix[0])
    
    first_row_zero = False
    first_col_zero = False
    
    // STEP 1: Check if the notice boards natively contain any bombs
    FOR r FROM 0 TO m - 1:
        IF matrix[r][0] == 0: first_col_zero = True
        
    FOR c FROM 0 TO n - 1:
        IF matrix[0][c] == 0: first_row_zero = True
        
    // STEP 2: Sweep the inner matrix and write to the notice boards
    FOR r FROM 1 TO m - 1:
        FOR c FROM 1 TO n - 1:
            IF matrix[r][c] == 0:
                matrix[r][0] = 0   // Mark the Row
                matrix[0][c] = 0   // Mark the Column
                
    // STEP 3: Obliterate the inner matrix based on our notes
    FOR r FROM 1 TO m - 1:
        FOR c FROM 1 TO n - 1:
            IF matrix[r][0] == 0 OR matrix[0][c] == 0:
                matrix[r][c] = 0
                
    // STEP 4: Clean up the notice boards
    IF first_row_zero == True:
        FOR c FROM 0 TO n - 1: matrix[0][c] = 0
        
    IF first_col_zero == True:
        FOR r FROM 0 TO m - 1: matrix[r][0] = 0
```

### 📊 Complexity Analysis
* **⏱️ Time Complexity:** $O(m \times n)$
    * We pass through the matrix just a few times.
    * Unlike the previous approaches, we completely eliminate the duplicate work of firing lasers immediately. A cell is only visited a constant number of times.
* **💾 Space Complexity:** $O(1)$
    * We strictly modified the input matrix in-place.
    * We only allocated two tiny boolean variables (**`first_row_zero`** and **`first_col_zero`**). Regardless of whether the grid is **`3x3`** or **`3000x3000`**, the extra memory used remains exactly the same. True $O(1)$ space!
---