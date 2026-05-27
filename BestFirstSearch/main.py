SuccList = {
    'A': [['B', 3], ['C', 2]],
    'B': [['A', 5], ['C', 2], ['D', 2], ['E', 3]],
    'C': [['A', 5], ['B', 3], ['F', 2], ['G', 4]],
    'D': [['H', 1], ['I', 99]],
    'F': [['J', 99]],
    'G': [['K', 99], ['L', 3]]
}

Start = 'A'
Goal = 'E'

Closed = list()

SUCCESS = True
FAILURE = False
State = FAILURE


# Generate next possible nodes
def MOVEGEN(N):
    New_list = list()
    if N in SuccList.keys():
        New_list = SuccList[N]
    return New_list


# Check goal condition
def GOALTEST(N):
    if N == Goal:
        return True
    else:
        return False


# Merge two lists
def APPEND(L1, L2):
    New_list = list(L1) + list(L2)
    return New_list


# Sort OPEN list based on heuristic value (cost)
def SORT(L):
    L.sort(key=lambda x: x[1])
    return L


# Best First Search Algorithm
def BestFirstSearch():

    # OPEN list starts with initial node
    OPEN = [[Start, 5]]

    CLOSED = list()

    global State
    global Closed

    # Loop until OPEN is empty or goal is found
    while (len(OPEN) != 0) and (State != SUCCESS):

        print("------------")

        # Pick first node (best candidate)
        N = OPEN[0]
        print("N =", N)

        # Remove selected node from OPEN
        del OPEN[0]

        # If goal found
        if GOALTEST(N[0]) == True:
            State = SUCCESS
            CLOSED = APPEND(CLOSED, [N])
            print("CLOSED =", CLOSED)

        else:
            # Add node to CLOSED list
            CLOSED = APPEND(CLOSED, [N])
            print("CLOSED =", CLOSED)

            # Generate child nodes
            CHILD = MOVEGEN(N[0])
            print("CHILD =", CHILD)

            # Remove already visited nodes from CHILD
            for val in CLOSED:
                if val in CHILD:
                    CHILD.remove(val)

            # Remove nodes already in OPEN
            for val in OPEN:
                if val in CHILD:
                    CHILD.remove(val)

            # Add remaining children to OPEN
            OPEN = APPEND(CHILD, OPEN)
            print("Unsorted OPEN =", OPEN)

            # Sort OPEN based on cost/heuristic
            SORT(OPEN)
            print("Sorted OPEN =", OPEN)

    Closed = CLOSED
    return State


# Driver Code
result = BestFirstSearch()

print(Closed, result)
