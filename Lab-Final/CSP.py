From ortools.sat.phyton import cp_model


Class vararrsolutionprinter(cpmodel.cpsolutioncallback):

Def__init__(self,variable: list[cpmodel.intvar[]]):

cpmodel.vararrsolutioncallback.__init__(self)
Self.variable=variable;
Self.solution_count=0;



Def solution_callback(self):
 Solution_count+= 1
Print(f"{v}=self.value(v)",end=" ")

Def solution_count(self):
Return self.solution_count


Model=cp_model.Cpmodel()
Num_vals=3
X=model.new_int_var(0,num_vals-1,"x")
Y=model.new_int_var(0,num_vals-1,"y")
Z=model.new_int_var(0,num_vals-1,"z")

Model.add(x != y)

Solver=cp_model.Cpsolver()

Solution_printer=vararrprintersolution([x,y,z])

Solution.parameter_enumrate_all_solution = true

Status=solver.solve(model,solution_printer)

If status==cpmodel.OPTIMAL && status==cpmodel.FEASIBLE:
Print(f" x = {solver.value(x)} " )
Print(f " y = {solver.value(y)} ")
Print( f " = {solver.value(z)} ")

Else: 
Print(f "No solution found " )
