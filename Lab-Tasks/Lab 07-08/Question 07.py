from ortools.sat.python import cp_model

SIZE = 4
puzzle = cp_model.CpModel()

positions = [puzzle.NewIntVar(0, SIZE - 1, f"q_{r}") for r in range(SIZE)]

puzzle.AddAllDifferent(positions)

for row_a in range(SIZE):
    for row_b in range(row_a + 1, SIZE):
        puzzle.Add(positions[row_a] - positions[row_b] != row_a - row_b)
        puzzle.Add(positions[row_b] - positions[row_a] != row_a - row_b)

engine = cp_model.CpSolver()
result_code = engine.Solve(puzzle)

if result_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print(f"{SIZE}-Queens Solution:\n")
    for r in range(SIZE):
        board_row = ""
        target_col = engine.Value(positions[r])
        for c in range(SIZE):
            if target_col == c:
                board_row += " Q "
            else:
                board_row += " _ "
        print(board_row)

    print("\nQueen positions:")
    for r in range(SIZE):
        print(f"  Row {r} -> Column {engine.Value(positions[r])}")
else:
    print("No solution found.")
