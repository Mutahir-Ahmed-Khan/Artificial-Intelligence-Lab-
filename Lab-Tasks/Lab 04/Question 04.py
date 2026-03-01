graph = {
'S':{'A':4,'B':2},
'A':{'C':5,'D':10},
'B':{'E':3},
'C':{'G':4},
'D':{'G':1},
'E':{'D':4},
'G':{}
}

def uniform_cost(source,target):

    pq = [(0, source, [source])]
    best_cost = {}

    while len(pq) != 0:

        pq = sorted(pq, key=lambda x: x[0])
        current_cost, current_node, route = pq.pop(0)

        if current_node == target:
            print("Path:", route)
            print("Total Cost:", current_cost)
            return

        prev = best_cost.get(current_node)

        if prev is None or current_cost < prev:
            best_cost[current_node] = current_cost

            neighbors = graph.get(current_node, {})
            for adj, weight in neighbors.items():
                updated_cost = current_cost + weight
                pq.append((updated_cost, adj, route + [adj]))


uniform_cost('S','G')
