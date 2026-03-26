game_tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

history_mm = []
history_ab = []
state_evals = {}
cuts = []

def compute_minimax(state, depth, top_turn):
    if depth == 0 or isinstance(state, int):
        history_mm.append(state)
        return state

    if top_turn:
        highest = -1000
        for branch in state:
            highest = max(highest, compute_minimax(branch, depth - 1, False))
        return highest
    else:
        lowest = 1000
        for branch in state:
            lowest = min(lowest, compute_minimax(branch, depth - 1, True))
        return lowest


def compute_alphabeta(state, depth, floor, ceiling, top_turn, label):
    if depth == 0 or isinstance(state, int):
        history_ab.append(state)
        return state

    if top_turn:
        val = -1000
        for idx, branch in enumerate(state):
            res = compute_alphabeta(branch, depth - 1, floor, ceiling, False, label + str(idx))
            val = max(val, res)
            floor = max(floor, val)

            if ceiling <= floor:
                cuts.append(label + " branch pruned")
                break

        state_evals[label] = val
        return val

    else:
        val = 1000
        for idx, branch in enumerate(state):
            res = compute_alphabeta(branch, depth - 1, floor, ceiling, True, label + str(idx))
            val = min(val, res)
            ceiling = min(ceiling, val)

            if ceiling <= floor:
                cuts.append(label + " branch pruned")
                break

        state_evals[label] = val
        return val


result_mm = compute_minimax(game_tree, 3, True)
result_ab = compute_alphabeta(game_tree, 3, -1000, 1000, True, "Root")

print("minimax root =", result_mm)
print("alpha-beta root =", result_ab)

print("\nminimax visited =", len(history_mm))
print("alpha-beta visited =", len(history_ab))

print("\nnode values =", state_evals)
print("\npruned nodes =", cuts)
