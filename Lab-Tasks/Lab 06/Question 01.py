import random

def f(x):
    return -x**2 + 6*x

def get_neighbors(x, x_min=0, x_max=6):
    neighbors = []
    if x - 1 >= x_min:
        neighbors.append(x - 1)
    if x + 1 <= x_max:
        neighbors.append(x + 1)
    return neighbors

def hill_climbing():
    x = random.randint(0, 6)
    print("Initial x:", x)
    print("f(x):", f(x))

    while True:
        neighbors = get_neighbors(x)
        best_neighbor = None
        best_value = f(x)

        for neighbor in neighbors:
            if f(neighbor) > best_value:
                best_value = f(neighbor)
                best_neighbor = neighbor

        if best_neighbor is None:
            break

        x = best_neighbor
        print("x:", x, "| f(x):", f(x))

    print("\nFinal Optimal x:", x)
    print("Maximum f(x):", f(x))

hill_climbing()
