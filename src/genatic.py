# the genatic algorithm consist of solutions that has chromosome that carry genes 
# here genes is places of queens on the board
# the implementaion consist of 6 main steps

# make populattion
# Select two parent chromosomes from a population according to their fitness (better the fitness, bigger the chance to be selected)
# crossover (Combine two individuals to create new individuals for possible inclusion in next generation)
# mutation (Each component of every individual is modified with by small probability)

from src.Nqueens import Nqueens as nq
from itertools import combinations
import random

# it takes 5 sec for 3400 generations and population_size = 55
# it takes 6 sec for 2000 generations and population_size = 100

def genatic(board_size, generations=2000, population_size=100, mut_prob = .5):


    """Generate an initial random population."""
    population = [nq(board_size) for _ in range(population_size)]

    for generation in range(generations):

        # sort the parents
        population = sorted(population,key= lambda p : p.conflicts())

        first = population[0].conflicts()
        if first == 0:
            print(f"Solution found in generation {generation}")
            return population[0]
        
        # print(first) # enable to see progress

        new_population = population[:10]  # Keep the best solution
        while len(new_population) < population_size:
            parent1 = random.choice(new_population)
            parent2 = random.choice(new_population)
            child = crossover(board_size, parent1, parent2)
            mutate(board_size, child, mut_prob)
            new_population.append(child)
    

        population = new_population
            
    print("No solution found.")
    return population[0]

def crossover(board_size,parent1,parent2):
    c = random.randint(1,board_size-1)
    child_pos = parent1.pos[:c] + parent2.pos[c:]
    return  nq(1,child_pos)

def mutate(board_size, child, mut_prob):
    if random.random() < mut_prob:
        child.changePos(random.randint(0,board_size-1),random.randint(0,board_size-1))
