# [💥 Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-interview-150)
Welcome to the grid, where a single zero can trigger a massive chain reaction! 🌐

### 🗺️ The Setup & The Rules
You are given an **`m x n`** integer matrix. Your mission is simple but highly destructive:
Scan the grid, and if you find a **`0`**, you must obliterate its **entire row and column**, turning every number in its crosshairs into a **`0`**. 🎯

#### ⚠️ The Ultimate Catch (The Space Challenge)
Anyone can solve this by creating a brand-new copy of the matrix (using $O(m \times n)$ extra space). A clever developer can solve it by keeping separate lists of the rows and columns that need to be zeroed out (using $O(m + n)$ extra space).

But you? You need to modify the grid **strictly in-place**.

Your true objective is to figure out how to orchestrate this chain reaction using a mind-bending $O(1)$ **constant extra space**! 🧠

#### 🧪 Target Practice (Examples)
- #### Example 1: The Single Strike ⚡
    A single zero sits dead center. Once triggered, it wipes out the middle row and the middle column in a perfect cross shape! <br><br>
    ![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

    > **Input:**
    > ```
    > [
    >   [1, 1, 1],
    >   [1, 0, 1],
    >   [1, 1, 1]
    > ]
    > ```
    > **Output:**
    > ```
    > [
    >   [1, 0, 1],
    >   [0, 0, 0],
    >   [1, 0, 1]
    > ]
    > ```

- #### Example 2: The Double Blast 💥💥
    Two zeroes are hiding in the top corners. Watch as their blast radii overlap to completely decimate the top row and outer columns! <br><br>
    ![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

    > **Input:**
    > ```
    > [
    >   [0, 1, 2, 0],
    >   [3, 4, 5, 2],
    >   [1, 3, 1, 5]
    > ]
    > ```
    > **Output:**
    > ```
    > [
    >   [0, 0, 0, 0],
    >   [0, 4, 5, 0],
    >   [0, 3, 1, 0]
    > ]
    > ```

#### 🚧 The Laws of Physics (Constraints)
Before you write your algorithm, keep the physical limits of our grid in mind:
* `m == matrix.length` *(Rows)*
* `n == matrix[0].length` *(Columns)*
* `1 <= m, n <= 200`
* `-2147483648 <= matrix[i][j] <= 2147483647` *(Standard 32-bit signed integers)*

### 🛣️ Approaches Comparison

#### 📊 Quick Reference Matrix

| Feature | 🛡️ Approach 1: Extra Space | 🐢 Approach 2: In-Place Marker | 🚀 Approach 3: FAANG Optimal |
| :--- | :--- | :--- | :--- |
| **Core Concept** | Create an identical `m x n` boolean matrix to track visited cells. | Use `None` as a temporary marker to avoid an extra matrix. | Use the grid's own first row/col as a "Notice Board". |
| **Time Complexity** | $O(m \times n \times (m+n))$ | $O(m \times n \times (m+n))$ | **$O(m \times n)$** |
| **Space Complexity**| $O(m \times n)$ | $O(1)$ | **$O(1)$** |
| **Grid Iterations** | Multiple nested sweeps. | Multiple nested sweeps. | Just 2 main passes! |
| **Drawback** | Fails the in-place constraint completely. Eats up RAM. | Terribly slow for grids with lots of zeroes (duplicate work). | Tricky edge cases with overlapping row/col `0` indices. |
| **Interview Value** | Baseline / Brute Force | Mid-level optimization | The "Hire This Person" solution |

#### [🛡️ Approach 1: The Safe Simulation](docs/extra-space.md)
**Best used when:** You just need a working solution fast, and memory constraints do not exist.
* **Pros:** Impossible to accidentally overwrite original data. Very easy to conceptualize and debug.
* **Cons:** Allocating a massive duplicate matrix in memory is an instant fail for the LeetCode follow-up constraint.

#### [🐢 Approach 2: The In-Place Marker](docs/inplace-simulation.md)
**Best used when:** You need to save memory, but can't quite remember the optimal trick.
* **Pros:** Achieves the $O(1)$ space constraint by temporarily changing data types to `None`.
* **Cons:** Every time it hits a `0`, it fires a laser beam across the entire row/col. If the grid is 90% zeroes, you are overwriting the exact same cells hundreds of times.

#### [🚀 Approach 3: The Notice Board Trick (Optimal)](docs/optimal-simulation.md)
**Best used when:** You want to ace a technical interview at a top-tier tech company.
* **Pros:** Achieves the holy grail: $O(1)$ space and $O(m \times n)$ time. By taking notes on the edges of the matrix first, we completely eliminate duplicate work!
* **Cons:** You have to be extremely careful not to accidentally overwrite the first row and column before you finish reading them.

### 📁 Repository Structure
```text
📦 set-matrix-zeroes
 ┣ 📂 docs
 ┃ ┣ 📜 extra-sapace.md                # 🛡️ Guide for the O(m*n) space brute-force
 ┃ ┣ 📜 inplace-simulation.md          # 🐢 Guide for the O(1) space 'None' trick
 ┃ ┗ 📜 optimal-simulation.md          # 🚀 Guide for the FAANG O(1) Notice Board trick
 ┣ 📂 source
 ┃ ┣ 📜 __init__.py                    # 📦 Makes source a Python package
 ┃ ┣ 📜 approaches.py                  # 🧠 The core algorithmic logic and lasers
 ┃ ┗ 📜 solution.py                    # 🔌 The clean LeetCode runner interface
 ┣ 📂 test
 ┃ ┣ 📜 __init__.py                    # 📦 Makes test a Python package
 ┃ ┣ 📜 cases.json                     # 🗃️ Edge cases, grids, and bomb placements
 ┃ ┗ 📜 test.py                        # 🚦 The automated dynamic test runner
 ┣ 📜 .gitignore                       # 🙈 Hides __pycache__ and system files
 ┗ 📜 README.md                        # 🌌 The master project landing page
```

#### 🚀 How to Run the Code
We built a dynamic test runner that will automatically ingest the **`cases.json`** file and test our optimal algorithms against the edge cases.

Open your terminal, navigate to the root of the repository (**`Set_Matrix_Zeroes/`**), and run:
```bash
# Run the test module
python3 -m test.test -v
```

---
