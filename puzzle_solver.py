from typing import List, Tuple, Set, Optional


#################################################################
# FILE : ex7.py
# WRITER : orin pour , orin1 , 207377649
# EXERCISE : intro2cs2 ex8 2021
# DESCRIPTION:this file ex8 file
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES: ...
#################################################################

# We define the types of a partial picture and a constraint (for type
# checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    counter = 0
    # if not black
    if picture[row][col] != 0:
        # count himself
        counter = 1
        not_legal = [0]
        # right
        counter += seen(picture, row, col, col + 1, len(picture[0]), 0, 'c',
                        not_legal)
        # left
        counter += seen(picture, row, col, col - 1, -1, 0, 'c', not_legal)
        # up
        counter += seen(picture, row, col, row + 1, len(picture), 0, 'r',
                        not_legal)
        # down
        counter += seen(picture, row, col, row - 1, -1, 0, 'r', not_legal)
    return counter


def seen(picture: Picture, row: int, col: int, start: int, end: int,
         counter: int, check, not_legal: List) -> int:
    step = 1
    if start > end:
        step = -1
    for x in range(start, end, step):
        if check == 'c':
            if picture[row][x] in not_legal:
                break
        if check == 'r':
            if picture[x][col] in not_legal:
                break
        counter += 1
    return counter


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    counter = 0
    # if white
    if picture[row][col] == 1:
        # count himself
        counter = 1
        not_legal = [0, -1]
        # right
        counter += seen(picture, row, col, col + 1, len(picture[0]), 0, 'c',
                        not_legal)
        # left
        counter += seen(picture, row, col, col - 1, -1, 0, 'c', not_legal)
        # up
        counter += seen(picture, row, col, row + 1, len(picture), 0, 'r',
                        not_legal)
        # down
        counter += seen(picture, row, col, row - 1, -1, 0, 'r', not_legal)
    return counter


def check_constraints(picture: Picture,
                      constraints_set: Set[Constraint]) -> int:
    returned_val = 1
    for constraint in constraints_set:
        row = constraint[0]
        col = constraint[1]
        seen_cells = constraint[2]
        max_seen = max_seen_cells(picture, row, col)
        min_seen = min_seen_cells(picture, row, col)
        if max_seen < seen_cells or min_seen > seen_cells:
            returned_val = 0
            return returned_val
        elif max_seen != min_seen:
            returned_val = 2
    return returned_val


def create_board(row: int, col: int) -> List[List[int]]:
    picture = []
    for r in range(row):
        temp_row = []
        for c in range(col):
            temp_row.append(-1)
        picture.append(temp_row)
    return picture


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[
    Picture]:
    picture = create_board(n, m)
    return _solve_puzzle_helper(constraints_set, n, m, picture, 0)


def _solve_puzzle_helper(constraints_set: Set[Constraint], n: int, m: int,
                         picture, ind) -> Optional[Picture]:
    row = ind // m
    col = ind % m
    if ind == m * n:
        return picture
    x = None
    for value in [0, 1]:
        picture[row][col] = value
        if check_constraints(picture, constraints_set):
            x = _solve_puzzle_helper(constraints_set, n, m, picture, ind + 1)
        if x is not None:
            return x
    picture[row][col] = -1
    return None


def _amount_of_solution_helper(constraints_set: Set[Constraint], n: int, m: int,
                         picture, ind:int, count:list) -> Optional[Picture]:
    row = ind // m
    col = ind % m
    if ind == m * n:
        count[0] += 1
        return count
    x = None
    for value in [0, 1]:
        picture[row][col] = value
        if check_constraints(picture, constraints_set):
            x = _amount_of_solution_helper(constraints_set, n, m, picture, ind + 1, count)
    picture[row][col] = -1
    return count


def how_many_solutions(constraints_set: Set[Constraint], n: int,
                       m: int):
    picture = create_board(n, m)
    count = _amount_of_solution_helper(constraints_set, n, m, picture, 0, [0])
    return count[0]


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    pass
