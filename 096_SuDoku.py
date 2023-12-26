'''
Joe Walter

difficulty: 25%
run time:   0:00
answer:     24702

    ***

096 Su Doku

Su Doku (Japanese meaning "number place") is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered "easy" because it can be solved by straight forward direct deduction.

The 6K text file contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

    ***

The following terminology is used throughout.

    grid      The 9x9 SuDoku puzzle
    block     One of the 3x3 sections with non-repeating values
    cell      Each square that has its own number
    row       A cell's row index
    col       A cell's column index

    number    The human-readable number that would be written down on paper
    code      The numbers associated with a cell, encoded in way that simplifies set operations
    value     Either a number or code depending on context
    correct   The number a cell takes in the final solution
    valid     A number that a cell could take without *immediately* violating any restriction
              (A correct number is valid, a valid number is not necessarily correct.)
              A code whose numbers are all valid
              A puzzle state containing only valid codes
    singular  A code representing only one number
    forced    A cell with one valid number

The valid numbers for each cell are encoded as a binary integer where
a 1 in the n-th digit place (1-indexed from the right) indicates n is valid.

Example: The code 011000101 indicates 1, 3, 7, and 8 are valid numbers for some cell.
         The code 111111111 indicates all numbers are valid.
         The code 000000000 is invalid.

The encoded values for every cell is stored as a 1D list. This is the puzzle state.

A depth-first search is performed to find the first (only) puzzle solution.
'''

from itertools import product
from copy import deepcopy

from data.p096 import get_data

#################################################################################
# Bit Operations

all_code = 2**9-1 # code representing all numbers are valid

def encode(n):
    ''' Convert human readable number to a singular code. '''
    return 1<<(n-1)

def decode(singular_code):
    ''' Convert a singular code to human readable number. '''
    return singular_code.bit_length()

def singular(code):
    ''' Determine if this code represents only one valid number. '''
    return code&(code-1) == 0 # and n != 0 # assumed

def remove_val(code, singular_code):
    ''' Remove a singular code from this code. '''
    return code&(all_code-singular_code)

def each_val(code):
    ''' Iterate through singular codes comprising this code. '''
    for shift in range(9):
        if (1<<shift)&code:
            yield (1<<shift)

#################################################################################
# Exceptions

class Solved(Exception):
    ''' The puzzle has been solved. '''
    def __init__(self, solution):
        self.solution = solution

#################################################################################
# Puzzle Class

class Puzzle:
    def __init__(self, arr):
        '''
        Create the SuDoku puzzle.

        arr is the 2D array of numbers indicating initial numbers. Blank spaces are indicated by 0s.
        '''
        self.state = [all_code]*81 # all numbers are valid for each cell in the grid
        self.count = 0             # how many cells are forced
        # Read in the list of numbers
        try:
            for row, col in product(range(9), repeat=2):
                if arr[row][col] == 0: continue # skip blank cells
                val = encode(arr[row][col])
                self.set(row, col, val)
        # The puzzle may be instantly solveable without any "guesses" needed.
        except Solved:
            pass

    def get(self, row, col):
        ''' Get the code at cell (row, col). '''
        return self.state[9*row+col]

    def set(self, row, col, code):
        ''' Set the cell at (row, col) to the code. '''
        # 0 indicates no valid numbers and is invalid.
        if code == 0:                    raise ValueError()
        if code == self.get(row, col):   return

        self.state[9*row+col] = code
        if singular(code):
            # The solution may have been reached.
            self.count += 1
            if self.solved():
                raise Solved(self)
            # Remove this singular code from the row.
            for i in range(9):
                if i == col: continue
                self.remove_value(row, i, code)
            # Remove this singular code from the col.
            for i in range(9):
                if i == row: continue
                self.remove_value(i, col, code)
            # Remove this singular code from the block.
            block_col, block_row = col//3*3, row//3*3
            for bc in range(block_col, block_col+3):
                for br in range(block_row, block_row+3):
                    if bc == col or br == row: continue
                    self.remove_value(br, bc, code)

    def remove_value(self, row, col, singular_code):
        ''' Remove the singular code from the code for the cell (row, col). '''
        code = self.get(row, col)
        new_c = remove_val(code, singular_code)
        self.set(row, col, new_c)

    def solved(self):
        ''' Retrurns true if the puzzle has been solved. Otherwise False. '''
        return self.count == 81

    def solve(self):
        ''' Solve the puzzle. Returns the 3-digit number in the top left corner. '''
        if not self.solved():
			# The recursive portion is put into _solve() so that
			# the Solved exception can be caught here at the top.
            try:
                self._solve()
            except Solved as e:
                self.state = e.solution.state
                self.count = e.solution.count # not necessary
        return self.triplet()

    def _solve(self):
        ''' The recursive portion of solve(). Basically depth-first search. '''
        # Loop through non-forced cells.
        for row, col in product(range(9), repeat=2):
            vals = self.get(row, col)
            if singular(vals): continue
            for val in each_val(vals):
				# Make a "guess" for this cell.
                try:
                    p = deepcopy(self)
                    p.set(row, col, val)
                    p._solve()
				# The guess led to an invalid state, so it is discarded.
                except ValueError:
                    self.remove_value(row, col, val)
            # No valid values for this cell means the puzzle state is invalid.
            raise ValueError()

    def __str__(self):
        ''' Convert to human readable string for printing. '''
        s = ""
        for row in range(9):
            for col in range(9):
                s += str(decode(self.get(row, col)))
            s += "\n"
        return s

    def triplet(self):
        ''' The 3 numbers in the top left corner. '''
        return     100 * decode(self.get(0, 0)) + \
                 10 * decode(self.get(0, 1)) + \
                  1 * decode(self.get(0, 2))

#################################################################################
# Main

ans = 0
for p in get_data():
    P = Puzzle(p)
    P.solve()
    # print(P)
    ans += P.triplet()
print(ans)
