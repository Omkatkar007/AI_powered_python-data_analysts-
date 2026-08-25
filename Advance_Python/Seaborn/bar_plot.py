import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
sns.barplot(x='sex', y='fare', data=df) 
plt.show()