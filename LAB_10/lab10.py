import matplotlib.pyplot as plt
import random
import math
import pandas as pd
import re

DATA_COM_SALE = pd.read_csv("company-sales_data.csv", delimiter=',')
DATA_TEXT = pd.read_csv("Text.txt", delimiter="\t")


def ex1():
    x = []
    for i in range(10000):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        x.append(die1 + die2)
    X = set(x)
    P = list([x.count(i) / len(x) for i in X])
    print(P)
    EX = 0
    for x in X:
        EX = EX + (x * P[x - 3])
    print(EX)

    VarX = 0
    for x in X:
        VarX = VarX + (x - EX) * (x - EX) * P[x - 3]
    print(VarX)

    SD = math.sqrt(VarX)
    print(SD)


def ex2():
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

    def pmf_normal(x, mu, sigma):
        return (1 / math.sqrt(2 * math.pi * pow(sigma, 2))) * math.exp(-(pow(x - mu, 2) / (2 * pow(sigma, 2))))

    def cdf_normal(x, mu, sigma):
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

    def plot_pmf_normal(mu, sigma):
        X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 100)
        P_normal = [pmf_normal(x, mu, sigma) for x in X]
        plt.plot(X, P_normal, '-')
        plt.title('PMF of Normal(%.2f, %.2f)' % (mu, sigma))
        plt.xlabel('X')
        plt.ylabel('P')
        plt.show()

    def plot_cdf_normal(mu, sigma):
        X = generator_data(mu - 4 * sigma, mu + 4 * sigma, 100)
        P_normal = [cdf_normal(x, mu, sigma) for x in X]
        plt.plot(X, P_normal, 'r-')
        plt.title('CDF of Normal(%.2f, %.2f)' % (mu, sigma))
        plt.xlabel('X')
        plt.ylabel('P')
        plt.show()

    def cau_c(mu, sigma):
        P_normal1 = cdf_normal(2, mu, sigma)
        P_normal2 = cdf_normal(7, mu, sigma)
        return P_normal2 - P_normal1

    plot_pmf_normal(0, 1.5)
    plot_cdf_normal(0, 1.5)
    print(cau_c(3, 4))


def ex3():
    facecream = DATA_COM_SALE.get("facecream", dict)
    shampoo = DATA_COM_SALE.get("shampoo", dict)
    toothpaste = DATA_COM_SALE.get("toothpaste", dict)
    month_number = DATA_COM_SALE.get("month_number", dict)

    plt.plot(month_number, toothpaste)
    plt.plot(month_number, shampoo)
    plt.plot(month_number, facecream)
    plt.legend(['Toothpaste', 'Shampoo', 'Facecream'])
    plt.show()


def ex4():
    data = DATA_TEXT.columns[0].lower()  # lưu dữ liệu file text vào data và chuyển chữ cái đầu thành chữ thường
    data_list = re.split(r'[^\w\-\']+', data)  # Tách dữ liệu thành mảng và lưu v data_list
    fig, ax = plt.subplots(1, 1)

    ax.hist(data_list, bins=30)
    plt.show()
