def linear_evolve(operator, state):
    res = [0.0] * len(operator)
    for i in range(len(operator)):
        for j in range(len(state)):
            res[i] += (operator[i][j] * state[j])
    return res
