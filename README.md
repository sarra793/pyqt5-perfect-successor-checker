# Perfect Successor Checker (PyQt5)

A desktop application built with **Python** and **PyQt5** that determines whether two positive integers form a **perfect digit succession**.

This educational project follows algorithmic programming principles commonly taught in the BAC SI curriculum, implementing all algorithms manually without using advanced Python built-in sorting functions.

## Features

- Simple graphical user interface (PyQt5)
- Positive integer input validation
- Manual bubble sort implementation
- Duplicate digit removal
- Perfect succession verification
- Reset and verification functionality

## Project Structure

```
.
├── main.py
├── InterfaceSuccession.ui
└── README.md
```

## Requirements

- Python 3.8 or later
- PyQt5

Install PyQt5:

```bash
pip install PyQt5
```

## Running the Application

```bash
python main.py
```

Make sure that `InterfaceSuccession.ui` is located in the same directory as `main.py`.

## How It Works

The application performs the following operations:

1. Reads two positive integers entered by the user.
2. Validates the input.
3. Concatenates both numbers.
4. Sorts all digits using a manually implemented Bubble Sort.
5. Removes duplicate digits.
6. Checks whether the remaining digits form a consecutive sequence.
7. Displays the result.

## Algorithm Overview

### Input Validation

Ensures that both inputs are positive decimal integers.

### Bubble Sort

Digits are sorted manually using the Bubble Sort algorithm without using:

- `sort()`
- `sorted()`
- `join()`

This respects educational programming constraints.

### Duplicate Removal

After sorting, repeated digits are removed while preserving ascending order.

### Perfect Succession Test

A sequence is considered perfect if every consecutive digit differs by exactly **1**.

For example:

- `12345` ✅
- `456789` ✅
- `1245` ❌

## Example

### Input

```
M = 123
N = 456
```

### Output

```
123 et 456 forment une succession parfaite (123456)
```

---

### Input

```
M = 145
N = 689
```

### Output

```
145 et 689 ne forment pas une succession parfaite (145689)
```

## Technologies Used

- Python
- PyQt5
- Qt Designer (.ui)

## Educational Objectives

This project demonstrates:

- Event-driven programming with PyQt5
- Modular programming
- String manipulation
- Manual sorting algorithms
- Input validation
- Algorithm implementation without relying on advanced Python built-ins

## License

This project is licensed under the MIT License.
