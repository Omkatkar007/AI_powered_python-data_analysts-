import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
sns.lineplot(x='age', y='fare', data=df,hue = 'sex')
plt.show()