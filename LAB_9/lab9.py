import matplotlib.pyplot as plt
import pandas as pd
import re

DATA_IRIS = pd.read_csv("iris.csv", delimiter=',')
DATA_COM_SALE = pd.read_csv("company-sales_data.csv", delimiter=',')
DATA_TEXT = pd.read_csv("Text.txt", delimiter="\t")


def ex1_1():
    sl = DATA_IRIS.sepal_length
    sw = DATA_IRIS.sepal_width
    fig = plt.figure(figsize=(3, 3))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.scatter(sl, sw)
    ax.set_xlabel('sepal_length')
    ax.set_ylabel('sepal_width')
    plt.show()


def ex1_2():
    fig, ax = plt.subplots(1, 1)
    a = DATA_IRIS.get("sepal_length", dict)
    ax.hist(a, bins=20)
    ax.set_xlabel('marks')
    plt.show()


def ex2_1():
    total_profit = DATA_COM_SALE.get("total_profit", dict)
    month_number = DATA_COM_SALE.get("month_number", dict)

    plt.plot(month_number, total_profit)
    plt.show()


def ex2_2():
    month_number = DATA_COM_SALE.get("month_number", dict)
    toothpaste = DATA_COM_SALE.get("toothpaste", dict)
    fig = plt.figure(figsize=(3, 3))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.scatter(month_number, toothpaste)
    plt.show()


def ex2_3():
    facecream = DATA_COM_SALE.get("facecream", dict)
    facewash = DATA_COM_SALE.get("facewash", dict)
    month_number = DATA_COM_SALE.get("month_number", dict)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(month_number, facecream, color='r', width=0.25)
    ax.bar(month_number + 0.25, facewash, color='b', width=0.25)
    ax.set_xticks([0.25, 1.25, 2.25, 3.25])
    ax.legend(labels=['FaceCream', 'FaceWash'])
    plt.show()


def ex3():
    def take_second(elem):
        return elem[1]

    data = DATA_TEXT.columns[0].lower()
    data_list = re.split(r'[^\w\-\']+', data)
    data_set = set(filter(None, data_list))

    result = []
    for item in list(data_set):
        index_value = [item, data_list.count(item)]
        result.append(index_value)

    result.sort(key=take_second, reverse=True)
    plt.plot([i[0] for i in result][0: 30], [i[1] for i in result][0: 30], marker='x', color='r')
    plt.show()
