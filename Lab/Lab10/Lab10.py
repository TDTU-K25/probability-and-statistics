import math
from matplotlib import pyplot as plt
import pandas as pd
import string
import numpy as np


def exercise1():
    x = np.random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 10000)

    X = set(x)
    print(X)

    P = []
    for i in X:
        count = 0
        for j in x:
            if (i == j):
                count += 1
        P.append(count / len(x))
    print(P)

    # Expectation
    EX = 0
    for x in X:
        EX = EX + (x * P[x - 2])
    print(EX)

    # Variance
    VarX = 0
    for x in X:
        VarX = VarX + (x - EX) * (x - EX) * P[x - 2]
    print(VarX)

    # Standard Deviation
    SD = math.sqrt(VarX)
    print(SD)


# exercise1()


def exercise2():
    def pmf_normal(x, mu, sigma):
        return (1 / math.sqrt(2 * math.pi * (sigma ** 2))) * (math.exp((- ((x - mu) ** 2) / (2 * (sigma ** 2)))))

    def cdf_normal(x, mu, sigma):
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

    def generator_data(a, b, size):
        n = (b - a) / (size - 1)
        result = []
        s = a
        while s < b:
            result.append(s)
            s = s + n
        if len(result) < size:
            result.append(b)
        return result

    def plot_pmf_normal(mu, sigma):
        X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
        P_normal = [pmf_normal(x, mu, sigma) for x in X]
        plt.plot(X, P_normal, '-')
        plt.title('PMF of Normal(%.2f, %.2f)' % (mu, sigma))
        plt.xlabel('X')
        plt.ylabel('P')
        plt.show()

    # ex2_a
    plot_pmf_normal(0, 1.5)

    def plot_cdf_normal(mu, sigma):
        X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 1000)
        P_normal = [cdf_normal(x, mu, sigma) for x in X]
        plt.plot(X, P_normal, '-', color='red')
        plt.title('CDF of Normal(%.2f, %.2f)' % (mu, sigma))
        plt.xlabel('X')
        plt.ylabel('P')
        plt.show()

    # ex2_b
    plot_cdf_normal(0, 1.5)

    def ex2_c():
        return cdf_normal(6, 3, 4) - cdf_normal(1, 3, 4)

    print(ex2_c())

# exercise2()


def exercise3():
    dataset_company_sales = pd.read_csv("company-sales_data.csv")

    month_number = dataset_company_sales['month_number']
    toothpaste_all_months = dataset_company_sales['toothpaste']
    shampoo_all_months = dataset_company_sales['shampoo']
    facecream_all_months = dataset_company_sales['facecream']

    plt.plot(month_number, toothpaste_all_months)
    plt.plot(month_number, shampoo_all_months)
    plt.plot(month_number, facecream_all_months)
    plt.legend(['toothpaste', 'shampoo', 'facecream'])
    plt.xlabel('Month')
    plt.ylabel('Units')
    plt.show()

# exercise3()


def exercise4(text):

    def remove_punctuation_and_lower(str):
        return str.translate(str.maketrans('', '', string.punctuation)).lower()

    text = remove_punctuation_and_lower(text)

    words = text.split(' ')

    # remove duplicate
    words_no_dup = list(dict.fromkeys(words))

    freq = []

    # count freq of each word
    for word in words_no_dup:
        count = 0
        for i in range(len(words)):
            if (word == words[i]):
                count += 1
        freq.append(count)

    df = pd.DataFrame({'words': words_no_dup, 'freqs': freq}
                      ).sort_values(by=['freqs'], ascending=False)

    ax = df.plot.hist(bins=30)
    plt.show()


# exercise4('Life is a mixture of ups and downs and one who has life must have seen various colours of life. Sometimes the colours are vivid and bright and sometimes they are just black and white. Life is a challenge and one who has the courage and strength to face it bravely is the one who goes through it and emerges as a great and successful person in life. Every person who has life is given various opportunities to make his life happy and prosperous and the one who understands this surely succeed in life. People who think that life is easy must know how people who don\'t have a home to live and food to eat survive on this planet. Life places us in different situations of sorrow, grief, happiness, defeat, love, hatred, failure, success and much more. So one must realize this fact that life is not a bed of roses, it even has thorns which we need to accept so that we do not get into a state of depression and face life with courage and vigour. There are times when we are happy about certain events in life and celebrate such occasions with great enthusiasm but we should not forget that life will not always give you fruits without sowing seeds from time to time. So, make sure you always make the best possible efforts to gain success in life as without efforts you cannot achieve anything in life. One must accept this bitter truth that good times and bad times never last forever so one should always be ready to face difficulties in life even if he\'s on the top of the world. And the one who is suffering from pain and misery should also know that there will be the time when all his sufferings will end and life will offer him new opportunities to succeed. Life is beautiful when you accept every little thing and ignore those that make you suffer. It\'s our own perspective that makes our life happy or miserable, so one must have a positive attitude towards life to make it happening and worthy.')
