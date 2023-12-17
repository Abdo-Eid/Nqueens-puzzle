from random import randint

# 2 queens can't be on the same
# row or column
# diagonal
# we'll make a DFS on the desicion tree
# but if there is an attack we won't continue
# and we'll back to the parent node
# then explore other children nodes


# after n = 10 it is very slow

def brute(board):
    n = board.n
    if n<4:
        return False
    col = set()
    posdiag = set()  # (col - row)
    negdiag = set()  # (col + row)
    res = []
    places = [None for _ in range(n)]

    # using backtracking
    def place_queen(row):
        if row == n:
            res.append(places.copy())  # Append a copy of places
            return

        for c in range(n):
            if c in col or (c - row) in posdiag or (c + row) in negdiag:
                continue

            # adding things to make sure not to step into them next time
            col.add(c)
            posdiag.add(c - row)
            negdiag.add(c + row)
            places[c] = row

            place_queen(row + 1)

            # removing sthings after getting a solution to get new one
            col.remove(c)
            posdiag.remove(c - row)
            negdiag.remove(c + row)
    # starting from raw 0 to n
    place_queen(0)
    return res

def display(sol):
    g = 0
    for s in sol:
        g +=1
        print(*s)

    print(g)

