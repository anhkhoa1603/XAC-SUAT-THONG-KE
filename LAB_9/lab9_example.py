import matplotlib.pyplot as plt
import numpy as np


# Line Charts
# Ex1
def ex1():
    samples = [.895, .91, .919, .926, .929, .931]
    plt.plot(samples)
    plt.show()


# Ex2
def ex2():
    years = [2010, 2011, 2012, 2013, 2014, 2015]
    samples = [.895, .91, .919, .926, .929, .931]
    plt.xlabel('Year')
    plt.ylabel('Yield')
    plt.plot(years, samples)
    plt.show()


# Ex3
def ex3():
    years = range(2000, 2012)
    apples = [.895, .91, .919, .926, .929, .931, .934, .936, .937, .9375, .9372, .94]
    oranges = [.962, .941, .93, .923, .918, .908, .907, .904, .901, .898, .9, .895]

    plt.plot(years, apples, marker='x')
    plt.plot(years, oranges, marker='o')
    plt.xlabel('Year')
    plt.ylabel('Yield')
    plt.title("Crop Yields in Kanto")
    plt.legend(['Apples', 'Oranges'])
    plt.show()

    plt.figure(figsize=(9, 3))
    plt.plot(years, apples, marker='x')
    plt.show()


# Scatter Plot
def scatter_plot():
    girls_grades = np.random.randint(100, size=30)
    boys_grades = np.random.randint(100, size=30)
    grades_range = np.random.randint(100, size=30)
    fig = plt.figure(figsize=(3, 3))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.scatter(grades_range, girls_grades, color='r')
    ax.scatter(grades_range, boys_grades, color='b')
    ax.set_xlabel('Grades range')
    ax.set_ylabel('Grades Scored')
    ax.set_title('scatter plot')
    plt.show()


def bar_graphs1():
    years = range(2000, 2006)
    oranges = [.4, .8, .9, .7, .6, .8]
    apples = [.35, .6, .9, .8, .65, .8]
    plt.xlabel('Year')
    plt.ylabel('Yield')
    plt.bar(years, oranges)
    plt.bar(years, apples, bottom=oranges)
    plt.show()


def bar_graphs2():
    data = [[30, 25, 50, 20], [40, 23, 51, 17]]
    x = np.arange(4)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(x + 0, data[0], color='b', width=0.25)
    ax.bar(x + 0.25, data[1], color='g', width=0.25)
    ax.set_xticks([0.25, 1.25, 2.25, 3.25])
    ax.set_xticklabels([2015, 2016, 2017, 2018])
    ax.legend(labels=['Oranges', 'Apples'])
    plt.show()


def histogram():
    fig, axes = plt.subplots(1, 1)
    a = np.array([72, 87, 5, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    axes.hist(a, bins=[0, 25, 50, 75, 100])
    axes.set_title("histogram of result")
    axes.set_xticks([0, 25, 50, 75, 100])
    axes.set_xlabel('marks')
    axes.set_ylabel('no. of students')
    plt.show()
