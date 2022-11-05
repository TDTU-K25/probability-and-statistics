from fractions import Fraction
import itertools
import random


def P(event, space):
    return Fraction(len(event & space), len(space))


""" Exercise 1 """

# a/ Both dice are the same


def simulator_dice1(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == dice2):
            count += 1
    return count / n


# b/ Both dice are different
def simulator_dice2(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 != dice2):
            count += 1
    return count / n

# c) Both dice are even


def simulator_dice3(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 == 0 and dice2 % 2 == 0):
            count += 1
    return count / n

# d) Both dice are odd


def simulator_dice4(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 % 2 != 0 and dice2 % 2 != 0):
            count += 1
    return count / n

# e) One dice is even and the other is odd


def simulator_dice5(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if ((dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0)):
            count += 1
    return count / n

# f/ Both dice are 6


def simulator_dice6(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 == 6 and dice2 == 6):
            count += 1
    return count / n

# g/ Summation of both dice are greater than 10


def simulator_dice7(n):
    count = 0
    for simulation in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1 + dice2 > 10):
            count += 1
    return count / n


""" Exercise 2 """


def cross(A, B):
    return {a + b for a in A for b in B}


def combos(items, n):
    return {' '.join(combo) for combo in itertools.combinations(items, n)}


urn = cross('B', '12') | cross('R', '123') | cross(
    'W', '12345')

u3 = combos(urn, 3)

# a/ All 3 balls are same color


def three_balls_same_color(n):
    count = 0
    for simulation in range(n):
        s = random.sample(u3, 1)[0]
        if (s.count('R') == 3 or s.count('W') == 3):
            count += 1
    return count / n

# b/ All 3 balls are different colors


def three_balls_different_color(n):
    count = 0
    for simulation in range(n):
        s = random.sample(u3, 1)[0]
        if s.count('B') == 1 and s.count('R') == 1 and s.count('W') == 1:
            count += 1
    return count / n

# c/ Only 2 balls are same color


def two_balls_same_color(n):
    count = 0
    for simulation in range(n):
        s = random.sample(u3, 1)[0]
        if s.count('B') == 2 or s.count('R') == 2 or s.count('W') == 2:
            count += 1
    return count / n

# d/ There are 2 red balls and 1 white ball


def r2w1(n):
    count = 0
    for simulation in range(n):
        s = random.sample(u3, 1)[0]
        if s.count('R') == 2 and s.count('W') == 1:
            count += 1
    return count / n

# e/ List all the cases that all 3 balls are white


def w3(n):
    count = 0
    for simulation in range(n):
        s = random.sample(u3, 1)[0]
        if s.count('W') == 3:
            count += 1
    return count / n


""" Exercise 3 """
ranks = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
suits = {'♡', '♢', '♣', '♠'}
cards = cross(ranks, suits)

four_cards = list(itertools.combinations(cards, 4))


def four_cards_same_suit(n):
    count = 0
    for simulation in range(n):
        s = random.sample(four_cards, 1)[0]
        AreFourCardsHaveSameSuit = True
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i][1] != s[j][1]:
                    AreFourCardsHaveSameSuit = False
                    break

        if (AreFourCardsHaveSameSuit):
            count += 1

    return count / n


def four_cards_different_suit(n):
    count = 0
    for simulation in range(n):
        s = random.sample(four_cards, 1)[0]
        AreFourCardsHaveDifferentSuit = True
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i][1] == s[j][1]:
                    AreFourCardsHaveDifferentSuit = False
                    break

        if (AreFourCardsHaveDifferentSuit):
            count += 1

    return count / n

# c/ All 4 cards are same color


def four_cards_same_color(n):
    count = 0
    for simulation in range(n):
        count_red = 0
        count_black = 0
        s = random.sample(four_cards, 1)[0]
        for card in s:
            if (card[1] == '♡' or card[1] == '♢'):
                count_red += 1
            if (card[1] == '♣' or card[1] == '♠'):
                count_black += 1

        if (count_red == 4 or count_black == 4):
            count += 1

    return count / n

# d/ All 4 cards are same value


def four_cards_same_value(n):
    count = 0
    for simulation in range(n):
        s = random.sample(four_cards, 1)[0]
        AreFourCardsHaveSameValue = True
        for i in range(0, len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i][0] != s[j][0]:
                    AreFourCardsHaveSameValue = False
                    break

        if (AreFourCardsHaveSameValue):
            count += 1

    return count / n

# e/ All 4 cards are numbers


def four_cards_are_numbers(n):
    count = 0
    ranks_not_number = ['1', 'J', 'Q', 'K']  # 1 represent for Ace
    for simulation in range(n):
        s = random.sample(four_cards, 1)[0]
        AreAllFourCardsNumber = True
        for card in s:
            for rank in ranks_not_number:
                if (card[0] == rank):
                    AreAllFourCardsNumber = False
                    break

        if (AreAllFourCardsNumber):
            count += 1
    return count / n


""" Exercise 4 """


URN = cross('W', '12') | cross('B', '123') | cross('R', '1234')

U3 = combos(URN, 3)


def white1blue1red1():
    return {s for s in U3 if s.count('W') == 1 and s.count('B') == 1 and s.count('R') == 1}


P = P(white1blue1red1(), U3)

""" Exercise 5 """
five_cards = list(itertools.combinations(cards, 5))

# a/ Theorical probability


def five_cards_straight():
    return None

# b/ Practical probability


def five_cards_straight(n):
    return None


""" Exercise 6 """
E = {0, 1, 2, 3, 4, 5}
# a/ List all 3-digits numbers in which every digit is an element in E


def three_digits_numbers():
    result = list(itertools.permutations(E, 3))

    # Xóa những trường hợp chữ số 0 đứng đầu
    for three_digits_number in result[::-1]:  # Duyệt list từ cuối lên đầu
        if (three_digits_number[0] == 0):
            result.remove(three_digits_number)

    return result

# b/ List all 4-digits numbers in which all digits are pairwise different and every digit is an element in E
# pairwise different: đôi một khác nhau


def four_digits_numbers():
    result = list(itertools.permutations(E, 4))

    # Xóa những trường hợp chữ số 0 đứng đầu
    for four_digits_number in result[::-1]:  # Duyệt list từ cuối lên đầu
        if (four_digits_number[0] == 0):
            result.remove(four_digits_number)

    # Xóa những trường hợp các chữ số không đôi một khác nhau
    for four_digits_number in result[::-1]:  # Duyệt list từ cuối lên đầu
        AreAllFourDigitsPairwiseDifferent = True
        for i in range(0, len(four_digits_number) - 1):
            for j in range(i + 1, len(four_digits_number)):
                if (four_digits_number[i] == four_digits_number[j]):
                    AreAllFourDigitsPairwiseDifferent = False
                    break

        if (AreAllFourDigitsPairwiseDifferent == False):
            result.remove(four_digits_number)

    return result
