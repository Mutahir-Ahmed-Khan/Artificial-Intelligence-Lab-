import random

# Fitness function f(x) = x^2 + 2x
def fitness(chromosome):
    x = int("".join(map(str, chromosome)),2)
    return x*x + 2*x

# Selection (Roulette Wheel)
def roulette_wheel_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [f/total_fitness for f in fitness_values]
    parents = random.choices(population, probabilities, k=2)
    return parents

# Crossover (Single Point)
def crossover(parent1,parent2):
    point = random.randint(1,len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1,child2

# Mutation
def mutate(chromosome,rate):
    for i in range(len(chromosome)):
        if random.random() < rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Genetic Algorithm
def genetic_algorithm(population,generations,mutation_rate):

    for g in range(generations):

        fitness_values = [fitness(c) for c in population]

        parents = roulette_wheel_selection(population,fitness_values)

        offspring = []
        for _ in range(len(population)//2):
            c1,c2 = crossover(parents[0],parents[1])
            offspring.append(c1)
            offspring.append(c2)

        population = [mutate(c,mutation_rate) for c in offspring]

    best = max(population,key=fitness)
    return best

# Random initial population
population = [[random.randint(0,1) for _ in range(5)] for _ in range(6)]

generations = 15
mutation_rate = 0.05

best = genetic_algorithm(population,generations,mutation_rate)

x = int("".join(map(str,best)),2)

print("Best chromosome:",best)
print("Best value of x:",x)
print("Best fitness value:",fitness(best))
