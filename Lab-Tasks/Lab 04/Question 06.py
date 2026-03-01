graph = {
'A':{'B':4,'C':2},
'B':{'E':12},
'C':{'D':3},
'D':{'G':4},
'E':{'G':5},
'G':{}
}

def a_star_search(source,target):

    open_nodes = [(0, 0, source, [source])]
    best_g = {}

    while len(open_nodes) > 0:

        open_nodes = sorted(open_nodes, key=lambda x: x[0])
        f_val, g_val, current, route = open_nodes.pop(0)

        if current == target:
            print("Path:", route)
            print("Cost:", g_val)
            return

        previous_cost = best_g.get(current)

        if previous_cost is None or g_val < previous_cost:
            best_g[current] = g_val

            neighbors = graph.get(current, {})
            for nxt, weight in neighbors.items():
                updated_g = g_val + weight
                updated_f = updated_g
                open_nodes.append((updated_f, updated_g, nxt, route + [nxt]))


a_star_search('A','G')

graph['A']['B'] = 8
graph['B']['E'] = 7

print("Edge cost changed")

a_star_search('A','G')
