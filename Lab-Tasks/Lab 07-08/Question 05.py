from ortools.sat.python import cp_model

cp_problem = cp_model.CpModel()

x = cp_problem.NewIntVar(0, 3, "A")
y = cp_problem.NewIntVar(0, 3, "B")
z = cp_problem.NewIntVar(0, 3, "C")

cp_problem.Add(x != y)
cp_problem.Add(y != z)
cp_problem.Add(x + y <= 4)

class ResultCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, targets):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.targets = targets
        self.count = 0

    def on_solution_callback(self):
        self.count += 1
        print(f"Solution {self.count}: ", end="")
        for item in self.targets:
            print(f"{item.Name()} = {self.Value(item)}", end="  ")
        print()

search_engine = cp_model.CpSolver()
search_engine.parameters.enumerate_all_solutions = True

observer = ResultCollector([x, y, z])
search_engine.Solve(cp_problem, observer)

print(f"\nTotal solutions found: {observer.count}")
