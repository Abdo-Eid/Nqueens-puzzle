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

def genatic(board_size, generations=9000, population=20, mutaion_probability = 5):

    selection_num = 10 # poplation is even selected is half
    
    mut_prob = ( mutaion_probability )/100 # mutaion change %

    # Start with a random population
    parents = [nq(board_size) for _ in range(population)]

    for _ in range(generations):
        # sort parents by fitness 
        parents_sorted = sorted(parents,key= lambda p : p.conflicts(),reverse=True)

        if not(parents_sorted[0].has_conflict()):
            return parents_sorted
            

        c = 3 # cross over point
        crossover(parents_sorted,selection_num,c,.4)
        mutation(parents_sorted,mut_prob,board_size)

    return parents_sorted

# make cross over with the first 'selection_num' parents
def crossover(parents,selection_num,c,c_prob):
    # get first selection_num random combination
    selected = random.sample(list(combinations(parents[:selection_num], 2)), selection_num)
    # crossover in place
    for s in selected:
        if random.random() > c_prob:
            continue
        s[0].pos[c:],s[1].pos[c:] = s[1].pos[c:],s[0].pos[c:]
        s[0].re_queen_pos()
        s[1].re_queen_pos()
    
def mutation(parents,mut_prob,board_size):
    for p in parents:
        if random.random() < mut_prob:
            p.pos[random.randint(0,board_size-1)] = random.randint(0,board_size-1)




s = genatic(5)
print(s[0])
print(s[0].conflicts())