# the genatic algorithm consist of solutions that has chromosome that carry genes 
# here genes is places of queens on the board
# the implementaion consist of 6 main steps

# make populattion
# Select two parent chromosomes from a population according to their fitness (better the fitness, bigger the chance to be selected)
# crossover (Combine two individuals to create new individuals for possible inclusion in next generation)
# mutation (Each component of every individual is modified with by small probability)

from Nqueens import Nqueens as nq
from itertools import combinations
import random

def genatic(board_size, generations=5000, population=25, mut_prob = .05):

    selection_num = 10 # poplation is even selected is half

    # Start with a random population
    parents = [nq(board_size) for _ in range(population)]
    parents_sorted = sorted(parents,key= lambda p : p.conflicts(),reverse=True)

    for _ in range(generations):

        selected = parents_sorted[:selection_num]

        # make cross over with the first 'selection_num' parents
        # get random index for cross over
        # the equation to be more likely to get first elements
        for _ in range(selection_num):
            rand_index = int(selection_num*(random.random()**7))
            rand_index2 = int(selection_num*(random.random()**6))
            if rand_index == rand_index2:
                continue
            # crossover in place

            c = random.randint(0,board_size-1)
            parents[rand_index].pos[c:],parents[rand_index2].pos[c:] = parents[rand_index2].pos[c:],parents[rand_index].pos[c:]
            parents[rand_index].re_queen_pos()
            parents[rand_index2].re_queen_pos()
        

        # mutation
        for p in parents_sorted:
            if random.random() < mut_prob:
                p.pos[random.randint(0,board_size-1)] = random.randint(0,board_size-1)

        # sort the parents
        parents_sorted = sorted(parents,key= lambda p : p.conflicts(),reverse=True)

        first = parents_sorted[0].conflicts()
        print(first)
            

        if first == 0:
            return parents_sorted

    return parents_sorted


    





s = genatic(5)
print(s[0])
print(s[0].conflicts())