# Visual Sudoku Solver  
*(Based on the exercise [Solucionador Visual de Sudoku](https://neps.academy/br/course/estrategias-avancadas-de-programacao/lesson/solucionador-visual-de-sudoku) from [Neps Academy](https://neps.academy))*

This project is a **command-line interactive application** written in **Python** that visually demonstrates how a **Sudoku puzzle is solved using recursive backtracking**. Instead of simply outputting the final solution, the program **animates the solving process in real time**, allowing the user to observe every tentative placement and backtracking step directly in the terminal. The project focuses on **algorithmic problem-solving**, **recursion**, and **constraint validation**, combined with a dynamic and visually pleasant **terminal-based interface** powered by the **Rich** library.

---

## Features

- Read a 9×9 Sudoku grid from standard input;
- Accept `.` or `0` as empty cells;
- Validate the input grid format before solving;
- Solve Sudoku puzzles using **recursive backtracking**;
- Visually animate each step of the algorithm in the terminal;
- Highlight the currently processed cell;
- Display real-time status messages (placements and backtracking);
- Control animation speed with a configurable delay;

---

## Algorithms and Concepts Used

- **Recursive Backtracking**  
  Explores all valid possibilities while respecting Sudoku constraints and backtracks upon conflicts.
- **Constraint Validation**  
  Ensures numbers are valid within:
  - Rows  
  - Columns  
  - 3×3 sub-grids  
- **Matrix Representation (2D List)**  
  Stores the Sudoku board as a 9×9 integer matrix.

---

## Terminal Visualization

The interface is built entirely for the **terminal**, using the **Rich** library:

- Side-by-side layout (Sudoku board+status panel);
- Highlighted cells for current operations;
- Dynamic updates using `Live` rendering;
- Clear visual separation of 3×3 sub-grids.

---

## How to Run

Follow the steps below to run the project locally.

```bash
git clone https://github.com/your-username/visual-sudoku-solver.git](https://github.com/maaluuzete/visual-sudoku-solver.git
cd visual-sudoku-solver
python -m venv venv
pip install -r requirements.txt
python main.py
```

## Input Format
When prompted, paste a Sudoku board using digits 1–9 and `.` or `0` for empty cells:
```
// example
53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
```
## Project Struture

```
visual-sudoku-solver/ 
│── main.py // Sudoku solver logic, recursive backtracking algorithm, and terminal visualization
│── requirements.txt 
│── README.md
```
