# Sudoku

puzzleIn is 2D array which contains 81 elements. The non-blank elements are the initial numbers that the Sudoku puzzle contains.

main is a 2D array where each of the 81 elements contains numbers that cannot be a solution to that location.

The not_to_actual function checks each element in main and, if any of the elements has 8 numbers then that means the solution at that location has been found.  
Every iteration of finding the solution the current state of the puzzle is output until the final solution is found.