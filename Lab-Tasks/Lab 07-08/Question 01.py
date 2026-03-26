data_tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

history = []

def run_minimax(state, depth_limit, maximizing_player):
    if depth_limit == 0 or isinstance(state, int):
        history.append(state)
        return state

    if maximizing_player:
        best_val = -float('inf')
        for branch in state:
            val = run_minimax(branch, depth_limit - 1, False)
            if val > best_val:
                best_val = val
        return best_val
    else:
        best_val = float('inf')
        for branch in state:
            val = run_minimax(branch, depth_limit - 1, True)
            if val < best_val:
                best_val = val
        return best_val

root_score = run_minimax(data_tree, 3, True)

print("part 1:")
print("root value =", root_score)

print("\npart 2:")
print("visited nodes =", history)

def run_limited_minimax(state, depth_limit, maximizing_player):
    if depth_limit == 0:
        if isinstance(state, list):
            curr = state
            while isinstance(curr, list):
                curr = curr[0]
            return curr
        return state

    if isinstance(state, int):
        return state

    if maximizing_player:
        best_val = -float('inf')
        for branch in state:
            val = run_limited_minimax(branch, depth_limit - 1, False)
            if val > best_val:
                best_val = val
        return best_val
    else:
        best_val = float('inf')
        for branch in state:
            val = run_limited_minimax(branch, depth_limit - 1, True)
            if val < best_val:
                best_val = val
        return best_val

depth_score = run_limited_minimax(data_tree, 2, True)
print("\npart 3:")
print("depth limited value =", depth_score)
