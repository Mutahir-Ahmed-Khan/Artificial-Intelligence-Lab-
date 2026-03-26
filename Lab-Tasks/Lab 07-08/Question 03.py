source_data = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

mm_log = []
ab_log = []
memo_ab = {}
prune_log = []

def run_mm(node, rem_depth, is_max_turn):
    if rem_depth == 0 or isinstance(node, int):
        mm_log.append(node)
        return node

    if is_max_turn:
        current_best = -1000
        for subtree in node:
            score = run_mm(subtree, rem_depth - 1, False)
            if score > current_best:
                current_best = score
        return current_best
    else:
        current_best = 1000
        for subtree in node:
            score = run_mm(subtree, rem_depth - 1, True)
            if score < current_best:
                current_best = score
        return current_best

def run_ab(node, rem_depth, a, b, is_max_turn, tag):
    if rem_depth == 0 or isinstance(node, int):
        ab_log.append(node)
        return node

    if is_max_turn:
        point = -1000
        for pos, subtree in enumerate(node):
            eval_score = run_ab(subtree, rem_depth - 1, a, b, False, tag + str(pos))
            if eval_score > point:
                point = eval_score
            if point > a:
                a = point
            if b <= a:
                prune_log.append(tag + " branch pruned")
                break
        memo_ab[tag] = point
        return point
    else:
        point = 1000
        for pos, subtree in enumerate(node):
            eval_score = run_ab(subtree, rem_depth - 1, a, b, True, tag + str(pos))
            if eval_score < point:
                point = eval_score
            if point < b:
                b = point
            if b <= a:
                prune_log.append(tag + " branch pruned")
                break
        memo_ab[tag] = point
        return point

out_mm = run_mm(source_data, 3, True)
out_ab = run_ab(source_data, 3, -1000, 1000, True, "Root")

print("minimax root =", out_mm)
print("alpha-beta root =", out_ab)

print("\nminimax visited =", len(mm_log))
print("alpha-beta visited =", len(ab_log))

print("\nnode values =", memo_ab)
print("\npruned nodes =", prune_log)
