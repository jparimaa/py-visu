import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def first_plot():
    iris = pd.read_csv('iris.data', names=[
                    'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    fig, ax = plt.subplots()

    # scatter the sepal_length against the sepal_width
    ax.scatter(iris['sepal_length'], iris['sepal_width'])
    # set a title and labels
    ax.set_title('Iris Dataset')
    ax.set_xlabel('sepal_length')
    ax.set_ylabel('sepal_width')
    plt.show()

def second_plot():
    x = np.linspace(0, 2, 100)

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(x, x, label='linear')  # Plot some data on the axes.
    ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
    ax.plot(x, x**3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    #ax.legend()  # Add a legend.
    plt.show()

def third_plot():
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 500

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()

third_plot()