import numpy as np
import pandas as pd
import math


def demo():
    df = pd.DataFrame(
        {'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']})
    print(df)

    df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': [
                      'red', 'white', 'blue']}, columns=['numbers', 'colors'])
    print(df)

    df = pd.DataFrame(
        np.random.randn(5, 3), columns=['N1', 'N2', 'N3'])
    print(df)

    df = pd.DataFrame({'N1': [1, 2, 3, 4], 'N2': [4, 3, 2, 1]})
    print(df)

    L = [{'Name': 'John', 'Last Name': 'Smith'},
         {'Name': 'Mary', 'Last Name': 'Wood'}]
    df = pd.DataFrame(L)
    print(df)

    data = np.loadtxt("sample.txt", delimiter=',')
    print(data)

    data = pd.read_csv("sample.txt", delimiter=',')
    print(data)

    data = pd.read_csv('sample1.txt', delimiter=',')
    print(data)
    print("Print column Score")
    print(data.Score)

    df = pd.DataFrame(np.random.randn(10, 3), columns=['N1', 'N2', 'N3'])
    print(df)

    print(df.head(5))

    print(df.tail(5))

    N2 = df['N2']
    print(N2)

    print(df[['N1', 'N2']])

    print(df[1:-2])


# demo()

""" Exercise 1 """


def exercise1():

    dataset_iris = pd.read_csv('iris.csv')

    # Hiển thị 5 dòng dữ liệu đầu tiên
    print(dataset_iris.head(5))

    def count(column):
        return len(column)

    def mean(column):
        sum = 0
        for row in column:
            sum += row
        return sum / count(column)

    def min(column):
        min = column[0]
        for row in column:
            if (min > row):
                min = row
        return min

    def max(column):
        max = column[0]
        for row in column:
            if (max < row):
                max = row
        return max

    def std(column):
        variance = 0
        for row in column:
            variance += ((row - mean(column)) ** 2)
        return math.sqrt(variance / count(column))

    sepal_length = dataset_iris['sepal_length']
    sepal_width = dataset_iris['sepal_width']
    petal_length = dataset_iris['petal_length']
    petal_width = dataset_iris['petal_width']

    df = pd.DataFrame({'sepal_length': [count(sepal_length), mean(sepal_length), std(sepal_length), min(sepal_length), max(sepal_length)], 'sepal_width': [count(sepal_width), mean(sepal_width), std(sepal_width), min(sepal_width), max(
        sepal_width)], 'petal_length': [count(petal_length), mean(petal_length), std(petal_length), min(petal_length), max(petal_length)], 'petal_width': [count(petal_width), mean(petal_width), std(petal_width), min(petal_width), max(petal_width)]}, index=['count', 'mean', 'std', 'min', 'max'])

    print(df)


# exercise1()


""" Exercise 2 """


def exercise2():

    dataset_population = pd.read_csv('population.csv')

    # Hiển thị 5 dòng dữ liệu đầu tiên
    print(dataset_population.head(5))

    countriesName = []
    for row in dataset_population['Country Name']:
        if row not in countriesName:
            countriesName.append(row)
    countriesName = sorted(countriesName)

    countriesCode = []
    for row in dataset_population['Country Code']:
        if row not in countriesCode:
            countriesCode.append(row)
    countriesCode = sorted(countriesCode)

    countByYear = dataset_population.groupby("Country Name")[
        "Year"].count()
    # SELECT [Country Name], COUNT(Year)
    # FROM dataset_population
    # GROUP BY [Country Name]
    countByYear = list(countByYear)

    meanByYear = dataset_population.groupby("Country Name")[
        "Value"].mean()
    meanByYear = list(meanByYear)

    minByYear = dataset_population.groupby("Country Name")[
        "Value"].min()
    minByYear = list(minByYear)

    maxByYear = dataset_population.groupby("Country Name")[
        "Value"].max()
    maxByYear = list(maxByYear)

    stdByYear = dataset_population.groupby("Country Name")[
        "Value"].std()
    stdByYear = list(stdByYear)

    df = pd.DataFrame({'Country name': countriesName, 'Country Code': countriesCode,
                      'Count': countByYear, 'Mean': meanByYear, 'Std': stdByYear, 'Min': minByYear, 'Max': maxByYear})
    print(df)


# exercise2()

# Don't use built-in function
def exercise2_v2():
    dataset_population = pd.read_csv('population.csv')
    dataset_population = dataset_population.sort_values('Country Name')

    # Hiển thị 5 dòng dữ liệu đầu tiên
    print(dataset_population.head(5))

    countriesName = []
    for row in dataset_population['Country Name']:
        if row not in countriesName:
            countriesName.append(row)
    countriesName = sorted(countriesName)

    countriesCode = []
    for row in dataset_population['Country Code']:
        if row not in countriesCode:
            countriesCode.append(row)
    countriesCode = sorted(countriesCode)

    def count():
        result = []
        count = 1
        i = 0
        while (i < len(dataset_population) - 1):
            if dataset_population.iloc[i]['Country Name'] == dataset_population.iloc[i + 1]['Country Name']:
                count += 1
                if (i == len(dataset_population) - 2):  # the last country
                    result.append(count)
            else:
                result.append(count)
                count = 1  # reset count for next country
            i += 1
        return result

    countByYear = count()

    def mean():
        result = []
        start_idx = 0
        i = 0  # index of list countByYear
        # end_idx - start_idx + 1 = number of time that country occurs in a file
        end_idx = countByYear[i] - 1
        sum = 0
        while (start_idx != len(dataset_population) - 1):
            while (start_idx <= end_idx):
                sum += dataset_population.iloc[start_idx].Value
                start_idx += 1
            result.append(sum / countByYear[i])
            i += 1
            if (i == len(countriesName)):  # Finish
                break
            sum = 0  # reset sum for next country
            end_idx = start_idx + countByYear[i] - 1
        return result

    meanByYear = mean()

    def std():
        result = []
        start_idx = 0
        i = 0  # index of list countByYear and list meanByYear
        end_idx = countByYear[i] - 1
        variance = 0
        while (start_idx != len(dataset_population) - 1):
            while (start_idx <= end_idx):
                variance += (
                    (dataset_population.iloc[start_idx].Value - meanByYear[i]) ** 2)
                start_idx += 1
            # standard deviation of sample
            result.append(math.sqrt(variance / (countByYear[i] - 1)))
            i += 1
            if (i == len(countriesName)):
                break
            variance = 0  # reset variance for next country
            end_idx = start_idx + countByYear[i] - 1
        return result

    stdByYear = std()

    def min():
        result = []
        start_idx = 0
        i = 0
        end_idx = countByYear[i] - 1
        min = dataset_population.iloc[0].Value
        while (start_idx != len(dataset_population) - 1):
            while (start_idx <= end_idx):
                if min > dataset_population.iloc[start_idx].Value:
                    min = dataset_population.iloc[start_idx].Value
                start_idx += 1
            result.append(min)
            i += 1
            if (i == len(countriesName)):
                break
            # reset min for next country
            min = dataset_population.iloc[start_idx].Value
            end_idx = start_idx + countByYear[i] - 1
        return result

    minByYear = min()

    def max():
        result = []
        start_idx = 0
        i = 0
        end_idx = countByYear[i] - 1
        max = dataset_population.iloc[0].Value
        while (start_idx != len(dataset_population) - 1):
            while (start_idx <= end_idx):
                if max < dataset_population.iloc[start_idx].Value:
                    max = dataset_population.iloc[start_idx].Value
                start_idx += 1
            result.append(max)
            i += 1
            if (i == len(countriesName)):
                break
            # reset max for next country
            max = dataset_population.iloc[start_idx].Value
            end_idx = start_idx + countByYear[i] - 1
        return result

    maxByYear = max()

    df = pd.DataFrame({'Country name': countriesName, 'Country Code': countriesCode, 'Count': countByYear,
                      'Mean': meanByYear, 'Std': stdByYear, 'Min': minByYear, 'Max': maxByYear})
    print(df)

# exercise2_v2()
