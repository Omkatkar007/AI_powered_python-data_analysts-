import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
sns.countplot(x='sex', data=df)
plt.show()