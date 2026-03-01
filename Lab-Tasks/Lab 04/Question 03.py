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

def limited_search(node,target,depth_limit,current_path,visited_nodes):

    visited_nodes.append(node)
    current_path.append(node)

    if node == target:
        print("Visited:", visited_nodes)
        print("Path:", current_path)
        return True

    if depth_limit == 0:
        current_path.pop()
        return False

    for nxt in graph.get(node,[]):
        if limited_search(nxt,target,depth_limit-1,current_path,visited_nodes):
            return True

    current_path.pop()
    return False


def iterative_deepening(source,destination,max_d):

    level = 0
    while level <= max_d:
        print("Depth Level:", level)
        if limited_search(source,destination,level,[],[]):
            return
        level += 1


iterative_deepening('A','G',5)
