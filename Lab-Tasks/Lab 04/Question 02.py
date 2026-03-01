graph = {
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':['G'],
'E':[],
'F':['H'],
'G':[],
'H':[]
}

def depth_limited(curr,target,maxdepth,track,seen):

    track = track + [curr]
    seen = seen + [curr]

    if curr == target:
        print("Visited:", seen)
        print("Path:", track)
        return True

    if maxdepth == 0:
        return False

    for child in graph.get(curr,[]):
        found = depth_limited(child,target,maxdepth-1,track,seen)
        if found:
            return True

    return False


print("Depth 2")
depth_limited('A','H',2,[],[])

print("Depth 3")
depth_limited('A','H',3,[],[])
