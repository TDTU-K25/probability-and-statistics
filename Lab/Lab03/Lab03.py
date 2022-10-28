import itertools
from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space) / len(space))


""" Exercise 1 """


def exercise1():
    S = {'MMM', 'MMF', 'MFM', 'MFF', 'FMM', 'FMF', 'FFM', 'FFF'}

    len_S = len(S)

    B = {s for s in S if 'F' in s}

    A = {s for s in S if s.count('F') == 3}

    P_B = P(B, S)

    P_A_B = P(A, S)

    P_A_with_B = P_A_B / P_B

    return P_A_with_B


print(exercise1())

""" Exercise 2 """


def exercise2():
    S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
         ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

    # A set doesn't allow duplicate value => use list
    A = [s for s in S if s[0] == 'Thanh']

    B = [s for s in S if s[1] == 'Nữ']

    A_B = []

    for i in A:
        for j in B:
            if (i[0] == j[0] and i[1] == j[1]):
                A_B.append(i)

    P_A = len(A) / len(S)

    P_B = len(B) / len(S)

    P_A_B = len(A_B) / len(S)

    P_A_with_B = P_A_B / P_B

    return P_A_with_B


print(exercise2())


""" Exercise 3"""


def exercise3():
    ranks = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
    suits = {'♠', '♣', '♦', '♥'}
    cards = list(itertools.product(ranks, suits))

    B = list(itertools.combinations(cards, 3))

    A1 = []

    for s in B:
        count = 0
        for card in s:
            if (card[0] == 'K'):
                count += 1
        if (count == 1 or count == 2):
            A1.append(s)

    A2 = []

    for s in B:
        count = 0
        for card in s:
            if (card[0] == 'K'):
                count += 1
        if (count >= 1):
            A2.append(s)

    P_A1 = len(A1) / len(B)
    P_A2 = len(A2) / len(B)

    print(round(P_A1, 4))
    print(round(P_A2, 4))


exercise3()
