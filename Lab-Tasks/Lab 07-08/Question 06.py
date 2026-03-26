from ortools.sat.python import cp_model

problem_instance = cp_model.CpModel()

var_a = problem_instance.NewIntVar(0, 20, "x")
var_b = problem_instance.NewIntVar(0, 20, "y")
var_c = problem_instance.NewIntVar(0, 20, "z")

problem_instance.Add(var_a + 2 * var_b + var_c <= 20)
problem_instance.Add(3 * var_a + var_b <= 18)

problem_instance.Maximize(4 * var_a + 2 * var_b + var_c)

engine = cp_model.CpSolver()
result_status = engine.Solve(problem_instance)

if result_status == cp_model.OPTIMAL:
    print("Optimal solution found!")
    print("x =", engine.Value(var_a))
    print("y =", engine.Value(var_b))
    print("z =", engine.Value(var_c))
    print("Optimal value (4x + 2y + z) =", engine.ObjectiveValue())
else:
    print("No optimal solution found.")
