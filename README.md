# Puzzley

A solver for the perpetual calendar puzzle that finds valid tile arrangements to display only the current day and month. Select any date and watch the algorithm solve the puzzle instantly or step-by-step with visual feedback.

---

## 🧩 About the Puzzle

The perpetual calendar puzzle is a classic desk puzzle with 8 polyomino pieces. The goal is to arrange the pieces on an irregular grid so that only the current day of the month and current month are left exposed, while all other months and days are covered.

The puzzle consists of:
- **12 month tiles** (January through December)
- **31 day tiles** (Days 1-31)
- **8 polyomino pieces** of varying shapes that you place to cover everything except the selected date

The grid has an irregular shape — it's mostly a 7x7 board with 2 spaces missing in the top right corner and 4 spaces missing across the bottom right.

---

## ✨ Features

- **Interactive GUI** — Select any day and month using a graphical interface
- **Automatic Solver** — Uses a backtracking algorithm to find valid solutions
- **Visual & Instant Modes** — Watch the pieces being placed in real-time or get instant results
- **Colorful Display** — Each piece is rendered in a different color for clarity
- **Multiple Piece Types** — 8 uniquely shaped tetromino and pentomino pieces with multiple orientations
- **Collision Detection** — The solver handles edge cases and wraparound prevention

---

## 🛠️ Technologies Used

- **Python** — Core solver logic
- **Pygame** — GUI and visualization
- **Backtracking Algorithm** — Efficient puzzle solving

---

## 📦 Requirements

- Python 3.x
- Pygame

Install dependencies:
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install pygame
```

---

## 🚀 Usage

Run the application:
```bash
python calendarPuzzle.py
```

### Controls

1. **Start Screen**
   - Click **"Run"** to enter date selection mode
   - Click **"Instant"** or **"Visual"** to toggle solving speed
   - Click **"Exit"** to close the application

2. **Date Selection**
   - Click a **month** tile to select the month
   - Click a **day** tile to select the day
   - Selected tiles highlight in orange

3. **Solving**
   - The solver automatically runs and displays the solution
   - **Visual Mode**: Watch pieces being placed one by one
   - **Instant Mode**: Get the solution immediately

4. **Reset**
   - Press **SPACEBAR** to return to the menu and start over

---

## 🧠 How It Works

The solver uses a **backtracking algorithm**:

1. Finds the first uncovered black tile (empty space)
2. Tries to place each remaining piece in all possible orientations
3. If placement succeeds, moves to the next empty space
4. If placement fails, backtracks and tries a different piece
5. Continues until all pieces are placed or no solution exists
6. Returns when all spaces (except the selected date) are covered

### Piece Definitions

The puzzle includes 8 different polyomino pieces with multiple orientations:
- **U-shape** (4 orientations)
- **L-shape** (8 orientations)
- **Zig-Zag** (8 orientations)
- **Corner** (4 orientations)
- **Z-shape** (4 orientations)
- **Rectangle** (2 orientations)
- **Pointer/T-shape** (8 orientations)
- **Arm/Plus-shape** (8 orientations)

---

## 📁 Project Structure

```
Puzzley/
├── calendarPuzzle.py      # Main solver and GUI application
├── requirements.txt       # Python dependencies
└── README.md
```

---

## 🎮 Gameplay Tips

- **Visual Mode** is slower but helps you understand how the solver works
- **Instant Mode** is best for quickly checking solutions
- Every date (except impossible combinations) has at least one valid solution
- The algorithm explores piece placements intelligently to minimize backtracking

---

## 📄 License

This project is open source and available under the terms specified in the repository.

---

**Built with 🧩 by DiamondHorizon**
