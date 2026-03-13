import heapq

goal=20
beam_width=2

def heuristic(n):
 return abs(goal-n)

def successors(x):
 return [x+2,x+3,x*2]

def beam_search(start):
 beam=[(heuristic(start),[start])]
 level=0

 while beam:
  print("Level",level)

  for h,path in beam:
   print(path[-1],"(h=",h,")")

  candidates=[]

  for h,path in beam:
   current=path[-1]

   if current==goal:
    return path

   for n in successors(current):
    newpath=path+[n]
    candidates.append((heuristic(n),newpath))

  beam=heapq.nsmallest(beam_width,candidates,key=lambda x:x[0])
  level+=1

 return None

start=1
path=beam_search(start)

print("\nFinal Path:")
print(path)
