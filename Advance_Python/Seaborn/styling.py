import seaborn as sns
import matplotlib.pyplot as plt

# first insigths are import then looks should be decicided 

df = sns.load_dataset('titanic')
sns.scatterplot(x='age', y='fare', data=df,
                hue = 'sex', style = 'sex', size = 'fare')
sns.set_theme(style="whitegrid")
plt.show()  