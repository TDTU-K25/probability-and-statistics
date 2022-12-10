import math
import numpy as np

""" Exercise 1 """


def exercise01():
    x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[
                         0.1, 0.2, 0.3, 0.2, 0.15, 0.05])

    # (a)
    X = set(x)
    print(X)

    # (b)
    P = []
    for i in X:
        count = 0
        for j in x:
            if (i == j):
                count += 1
        P.append(count / len(x))
    print(P)

    # (c)

    # Expectation
    EX = 0
    for x in X:
        EX = EX + (x * P[x])
    print(EX)

    # Variance
    VarX = 0
    for x in X:
        VarX = VarX + (x - EX) * (x - EX) * P[x]
    print(VarX)

    # Standard Deviation
    SD = math.sqrt(VarX)
    print(SD)

    # (d) Calculate the probability of having 3 or more emergency cases
    P_X_3 = P[3] + P[4] + P[5]
    print(P_X_3)

# exercise01()


""" Exercise 2 """


def exercise02():
    # (a)
    x = np.random.choice([0, 1, 2], 10000, p=[0.25, 0.5, 0.25])

    # (b)
    X = set(x)
    print(X)

    # (c)
    P = []
    for i in X:
        count = 0
        for j in x:
            if (i == j):
                count += 1
        P.append(count / len(x))
    print(P)

    # (d)

    # Expectation
    EX = 0
    for x in X:
        EX = EX + (x * P[x])
    print(EX)

    # Variance
    VarX = 0
    for x in X:
        VarX = VarX + (x - EX) * (x - EX) * P[x]
    print(VarX)

    # Standard Deviation
    SD = math.sqrt(VarX)
    print(SD)

    # (e) Calculate the probability to have at least one head
    P_X_1 = P[1] + P[2]
    print(P_X_1)

# exercise02()
