# Alpha–Beta Pruning AI (Tic-Tac-Toe Demonstration)

## 📌 Overview

This project implements the **Alpha–Beta Pruning optimization** over the classical **Minimax adversarial search algorithm**.
The implementation demonstrates how pruning reduces the number of explored nodes while still guaranteeing optimal play in deterministic, perfect-information games.

The program uses **Tic-Tac-Toe** as a working example, implemented in **pure Python** with:

- Recursive Minimax search
- Alpha (α) and Beta (β) pruning bounds
- Evaluation function
- Depth control
- Node-count statistics for experimentation

This work is completed as part of:

**Department of Computer Science**
**Introduction to Artificial Intelligence – Group Assignment**

---

## 🎮 Demonstrated Game

Tic-Tac-Toe is chosen because:

- It is simple enough to implement clearly
- It has a manageable state space
- It allows focus on **algorithm reasoning**, not UI complexity
- Results are easy to verify

---

## ✅ Features

- ✔ Alpha–Beta Pruning algorithm
- ✔ Perfect-play AI for both MAX and MIN
- ✔ Automatic game simulation
- ✔ Node evaluation counter (important for report analysis)
- ✔ Fully recursive and readable

---

## 🧠 Core Idea

Minimax evaluates all possible game states to choose an optimal move, but:

```
Time Complexity = O(b^d)
```

Alpha–Beta introduces bounds:

- **α** → best value MAX can guarantee
- **β** → best value MIN can guarantee

If at any point:

```
alpha >= beta
```

Further exploration is useless — the branch is **pruned**.

With good move ordering:

```
Effective Complexity ≈ O(b^(d/2))
```

Meaning **double the search depth for the same cost** in practice.

---

## 🏃 Running the Program

### Requirements

Only **Python 3.x** is needed.

No external libraries required.

### Run

```
python alpha_beta_tictactoe.py
```

The program will:

- Play MAX (X) vs MIN (O)
- Print each move
- Print number of evaluated nodes per turn
- Show final board & winner

---

## 🔬 Experimental Observations

From multiple runs on sample trees:

| Aspect                  | Observation                           |
| ----------------------- | ------------------------------------- |
| Minimax Baseline        | Explores very large number of nodes   |
| Alpha–Beta              | Reduces explored states significantly |
| With good move ordering | Very high pruning efficiency          |
| With poor ordering      | Less pruning (still correct)          |
| Execution speed         | Noticeably faster                     |
| Depth reach             | Deeper search possible                |

Sample Output Example:

```
MAX chooses move 0
Nodes evaluated this turn: 78

MIN chooses move 4
Nodes evaluated this turn: 23
```

This empirical result supports the theoretical claim discussed in the report.

---

## ⚙️ Implementation Choices

- Pure Python for clarity and compliance
- Simple static evaluation function:

  - +1 if MAX wins
  - −1 if MIN wins
  - 0 otherwise

- Depth parameter to control computation
- Separate game environment class
- Clean separation of logic

Stopping Conditions:

1. Depth reached
2. Terminal state reached
3. No available moves

---

## ⛔ Limitations

- Still exponential worst-case if ordering is bad
- Only suitable for:

  - Deterministic games
  - Perfect-information games

- Not ideal for:

  - Games with chance (dice)
  - Hidden-information games
  - Extremely large branching factors

- Requires careful recursive design

These are also discussed in detail in the report.

---

## 📚 References

- Russell, S. & Norvig, P. _Artificial Intelligence: A Modern Approach_
- Stanford University — CS221 Game Playing Notes
- Classical AI Search Literature
- University of Bolton Report Writing Guidelines

## Group Members:

1. Abduraheem Muzemil   UGR/8538/14  
2. Abdulnur Hussein    UGR/9498/15  
3. Akrem Omer          UGR/1192/14  
4. Khalid Muzemil      UGR/4405/14

