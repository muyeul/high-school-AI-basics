import pandas as pd

iris = pd.read_csv('Iris.csv')

print(iris.head(2))
print(iris.info( ))
print(iris.describe( ))
