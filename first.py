import pandas as pd
import os
import matplotlib.pyplot as plt


cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

iris = pd.read_csv('iris.data', names=[
                   'sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head())


fig, ax = plt.subplots()

# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
plt.show()