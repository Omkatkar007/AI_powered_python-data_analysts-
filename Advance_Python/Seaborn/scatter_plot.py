import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
sns.scatterplot(x='sepal_length', y='sepal_width', data=df,
                hue = 'species', style = 'species', size = 'petal_length')

plt.show()