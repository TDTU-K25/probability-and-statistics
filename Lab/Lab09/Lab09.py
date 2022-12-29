import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string


def exercise1():
    dataset_iris = pd.read_csv("iris.csv")

    sepal_length = dataset_iris['sepal_length']
    sepal_width = dataset_iris['sepal_width']

    def simpleScatterPlot():
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.scatter(sepal_length, sepal_width, color='r')
        ax.set_xlabel('sepal_length')
        ax.set_ylabel('sepal_width')
        ax.set_title('Scatter Plot')
        plt.show()

    simpleScatterPlot()

    print()

    def histogram():
        fig, ax = plt.subplots(1, 1)
        a = np.array(sepal_length)
        ax.hist(a, bins=20)
        ax.set_title("Histogram of Result")
        ax.set_xlabel('sepal_length')
        ax.set_ylabel('No. of sepal_length')
        plt.show()

    histogram()


# exercise1()


def exercise2():
    dataset_company_sales = pd.read_csv("company-sales_data.csv")

    toothpaste_all_months = dataset_company_sales['toothpaste']
    total_profit_all_months = dataset_company_sales['total_profit']

    def part1():
        plt.xlabel('Month')
        plt.ylabel('Total Profit')
        plt.title("Total Profit Of All Months")
        plt.plot(total_profit_all_months)
        plt.show()

    part1()

    def part2():
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_axes([0, 0, 1, 1])
        ax.scatter(toothpaste_all_months, total_profit_all_months, color='r')
        ax.set_xlabel('Toothpaste')
        ax.set_ylabel('Total Profit')
        ax.set_title('Scatter Plot')
        plt.show()

    part2()

    def part3():
        dataset_company_sales.plot(x="month_number", y=[
                                   "facecream", "facewash"], kind="bar", rot=0, xlabel='Month', ylabel='No. Of Products')
        plt.show()

    part3()


# exercise2()

def exercise3(text):

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

    # x-axis is index value of each word
    ax = df.head(30).plot.line()
    plt.xlabel('Index')
    plt.ylabel('Frequency')
    plt.show()


# exercise3('Life is a mixture of ups and downs and one who has life must have seen various colours of life. Sometimes the colours are vivid and bright and sometimes they are just black and white. Life is a challenge and one who has the courage and strength to face it bravely is the one who goes through it and emerges as a great and successful person in life. Every person who has life is given various opportunities to make his life happy and prosperous and the one who understands this surely succeed in life. People who think that life is easy must know how people who don\'t have a home to live and food to eat survive on this planet. Life places us in different situations of sorrow, grief, happiness, defeat, love, hatred, failure, success and much more. So one must realize this fact that life is not a bed of roses, it even has thorns which we need to accept so that we do not get into a state of depression and face life with courage and vigour. There are times when we are happy about certain events in life and celebrate such occasions with great enthusiasm but we should not forget that life will not always give you fruits without sowing seeds from time to time. So, make sure you always make the best possible efforts to gain success in life as without efforts you cannot achieve anything in life. One must accept this bitter truth that good times and bad times never last forever so one should always be ready to face difficulties in life even if he\'s on the top of the world. And the one who is suffering from pain and misery should also know that there will be the time when all his sufferings will end and life will offer him new opportunities to succeed. Life is beautiful when you accept every little thing and ignore those that make you suffer. It\'s our own perspective that makes our life happy or miserable, so one must have a positive attitude towards life to make it happening and worthy.')
