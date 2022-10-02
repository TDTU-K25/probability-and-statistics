from fractions import Fraction
import itertools
import random


def P(event, space):
    return Fraction(len(event & space), len(space))


def cross(A, B):
    return {a + b for a in A for b in B}


def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}


""" Exercise 1 """


def simulator_dice1(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0 and dice2 % 2 == 0):
            count += 1
    return count / n

# print(simulator_dice1(10))
# print(simulator_dice1(100))
# print(simulator_dice1(1000))
# print(simulator_dice1(10000))
# print(simulator_dice1(100000))
# print(simulator_dice1(1000000))


""" Exercise 2 """


def simulator_dice2(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0):
            count += 1
    return count / n

# print(simulator_dice2(10))
# print(simulator_dice2(100))
# print(simulator_dice2(1000))
# print(simulator_dice2(10000))
# print(simulator_dice2(100000))
# print(simulator_dice2(1000000))


""" Exercise 3 """


def simulator_dice3(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == dice2):
            count += 1
    return count / n

# print(simulator_dice3(10))
# print(simulator_dice3(100))
# print(simulator_dice3(1000))
# print(simulator_dice3(10000))
# print(simulator_dice3(100000))
# print(simulator_dice3(1000000))


""" Exercise 4 """


def simulator_dice4(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == 1 and dice2 == 6) or (dice1 == 6 and dice2 == 1):
            count += 1
    return count / n

# print(simulator_dice4(10))
# print(simulator_dice4(100))
# print(simulator_dice4(1000))
# print(simulator_dice4(10000))
# print(simulator_dice4(100000))
# print(simulator_dice4(1000000))


""" Exercise 5 """


def simulator_dice5(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2 > 6):
            count += 1
    return count / n

# print(simulator_dice5(10))
# print(simulator_dice5(100))
# print(simulator_dice5(1000))
# print(simulator_dice5(10000))
# print(simulator_dice5(100000))
# print(simulator_dice5(1000000))


""" Exercise 6 """
ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = list(itertools.product(ranks, suits))


def simulator_poker1(n):
    count = 0
    for simulation in range(n):
        # Generate 5 số ngẫu nhiên khác nhau trong khoảng từ 0 đến 51
        choose_five_cards = random.sample(range(0, 52), 5)

        # flag kiểm tra xem cả 5 lá bài đều có chất cơ hay không
        AreAllOfFiveCardsAreHeart = True

        for index in choose_five_cards:
            if cards[index][1] != '♡':
                AreAllOfFiveCardsAreHeart = False
                break

        if (AreAllOfFiveCardsAreHeart):
            count += 1

    return count / n


# print(simulator_poker1(10))
# print(simulator_poker1(100))
# print(simulator_poker1(1000))
# print(simulator_poker1(10000))
# print(simulator_poker1(100000))
# print(simulator_poker1(1000000))


""" Exercise 7 """


def simulator_poker2(n):
    count = 0
    for simulation in range(n):
        choose_four_cards = random.sample(range(0, 52), 4)

        AreFourCardsHaveDifferentTypes = True

        # Lấy 1 trong 4 lá bài đã rút và so sánh với các lá bài còn lại xem có khác chất không
        for i in range(0, len(choose_four_cards) - 1):
            for j in range(i + 1, len(choose_four_cards)):
                if cards[choose_four_cards[i]][1] == cards[choose_four_cards[j]][1]:
                    AreFourCardsHaveDifferentTypes = False
                    break

        if (AreFourCardsHaveDifferentTypes):
            count += 1
    return count / n


# print(simulator_poker2(10))
# print(simulator_poker2(100))
# print(simulator_poker2(1000))
# print(simulator_poker2(10000))
# print(simulator_poker2(100000))
# print(simulator_poker2(1000000))


""" Exercise 8 """

urn = cross('W', '12345678') | cross('B', '123456') | cross(
    'R', '123456789')

U6 = combos(urn, 6)

w2b2r2 = {s for s in U6 if s.count('W') == 2 and s.count(
    'B') == 2 and s.count('R') == 2}
# print(P(w2b2r2, U6))
