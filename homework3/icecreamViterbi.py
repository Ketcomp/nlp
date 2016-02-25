def bestSequenceFor(observation, a, b):
    viterbi = [[None for x in range(observation.__len__())] for y in range(0, 4)]  # Ignore 0th element
    backPointers = [[None for x in range(observation.__len__())] for y in range(0, 4)]  # Ignore 0th element

    # Initialization
    for state in range(1, 3):
        viterbi[state][1] = a[0][state] * b[state][observation[1]] # Consider State #1 Hot and #2 as Cold state
        backPointers[state][1] = 0

    # Recursion step
    for t in range(2, 10): # Loop it for (2 to N)
        for s in range(1, 3):
            viterbi[s][t] = max( (viterbi[1][t - 1] * a[1][s] * b[s][observation[t]]),
                                 (viterbi[2][t - 1] * a[2][s] * b[s][observation[t]]) )
            hot = viterbi[1][t - 1] * a[1][s] * b[s][observation[t]]
            cold = viterbi[2][t - 1] * a[2][s] * b[s][observation[t]]
            # If the larger value is from Hot state, then Hot else Cold.
            backPointers[s][t] = 1 if (hot - cold)>0 else 2

    # Termination step
    viterbiFinal = max( (viterbi[1][9]),(viterbi[2][9]) )
    hot = viterbi[1][9]
    cold = viterbi[2][9]
    backPointersFinal = 1 if (hot - cold)>0 else 2

    return backPointers[1] if(backPointersFinal==1) else backPointers[2]

def printResult(result):
    result = result[1:] # Remove the 'None' element
    # Reverse the list to get the actual order of states
    result = list(reversed(result))
    for value in result:
        if value == 1:
            print('H', end=" ")
        elif value == 2:
            print('C', end=" ")
        else:
            print('', end=" ")
    print("")

if __name__ == '__main__':
    observation1 = [0, 3, 3, 1, 1, 2, 2, 3, 1, 3] # Pad an extra zero in the beginning to prevent indexing issues.
    observation2 = [0, 3, 3, 1, 1, 2, 3, 3, 1, 2]

    # Consider #1 Hot and #2 as Cold state
    a = [[1.0, 0.8, 0.2],  # Probability from start-state to #1 and #2
         [1.0, 0.7, 0.3],  # ...from #1 to itself & #1 to #2
         [1.0, 0.4, 0.6]]  # ...from #2 to #1 & #2 to itself

    b = [[1.0, 1.0, 1.0, 1.0],
         [1.0, 0.2, 0.4, 0.4],  # Probabilities of HOT state
         [1.0, 0.5, 0.4, 0.1],  # Probablities of COLD state
         [1.0, 1.0, 1.0, 1.0]]

    result1 = bestSequenceFor(observation1, a, b)
    printResult(result1)
    result2 = bestSequenceFor(observation2, a, b)
    printResult(result2)
