maze = [
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0]
]

goals = [(0,3),(3,2)]
start = (0,0)

def manhattan(p,q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def greedy_search(src,dest):

    open_list = [(manhattan(src,dest), src, [src])]
    closed = set()

    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    while len(open_list) > 0:

        open_list = sorted(open_list, key=lambda x: x[0])
        h_val, current, route = open_list.pop(0)

        if current == dest:
            return route

        closed.add(current)

        for step in moves:
            nr = current[0] + step[0]
            nc = current[1] + step[1]

            if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                if maze[nr][nc] == 0 and (nr,nc) not in closed:
                    new_path = route + [(nr,nc)]
                    open_list.append((manhattan((nr,nc),dest),(nr,nc),new_path))


complete_path = []
position = start

for target in goals:
    segment = greedy_search(position,target)
    if segment:
        complete_path.extend(segment)
        position = target

print("Path covering all goals:", complete_path)
