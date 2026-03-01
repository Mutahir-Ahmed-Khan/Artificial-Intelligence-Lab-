building = [
[1,1,0,1],
[0,1,1,1],
[1,1,0,1],
[1,0,1,1]
]

def make_graph(mat):
    g = {}
    r = len(mat)
    c = len(mat[0])

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    for row in range(r):
        for col in range(c):
            if mat[row][col] == 1:
                pos = (row,col)
                g[pos] = []

                for d in directions:
                    nr = row + d[0]
                    nc = col + d[1]

                    if nr >= 0 and nr < r and nc >= 0 and nc < c:
                        if mat[nr][nc] == 1:
                            g[pos].append((nr,nc))
    return g


def breadth_first(g,start,end):
    seen = set()
    q = [(start,[start])]

    while len(q) > 0:
        current , route = q.pop(0)

        if current in seen:
            continue

        seen.add(current)

        if current == end:
            print("Traversal:", list(seen))
            print("Shortest Path:", route)
            return

        for adj in g.get(current,[]):
            if adj not in seen:
                q.append((adj, route + [adj]))


graph = make_graph(building)
breadth_first(graph,(0,0),(3,3))
