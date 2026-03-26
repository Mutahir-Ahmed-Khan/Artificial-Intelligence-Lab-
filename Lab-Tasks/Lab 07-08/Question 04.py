from ortools.sat.python import cp_model

engine = cp_model.CpModel()

var_x = engine.NewIntVar(0, 3, "var_x")
var_y = engine.NewIntVar(0, 3, "var_y")
var_z = engine.NewIntVar(0, 3, "var_z")

engine.Add(var_x != var_y)
engine.Add(var_y != var_z)
engine.Add(var_x + var_y <= 4)

processor = cp_model.CpSolver()
outcome = processor.Solve(engine)

if outcome in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print("A =", processor.Value(var_x))
    print("B =", processor.Value(var_y))
    print("C =", processor.Value(var_z))
else:
    print("No solution found.")
