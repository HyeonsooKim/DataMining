import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

plt.style.use('seaborn')
sns.set(font_scale=2.5)

data = pd.read_csv('../data/train.csv')

for col in data.columns:
    print('column: {:>12} percent of NaN value: {:.2f}%'.format(col, 100 * (data[col].isnull().sum() / data[col].shape[0])))

print(data.iloc[:, 0:5])
print(data.loc[:, ['PassengerId', 'Cabin']])

# msno.matrix(df=data.iloc[:, :], figsize=(8, 8))
# plt.show()

f, ax = plt.subplots(1, 2, figsize=(18, 8))
data['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
ax[0].set_title('Pie plot - Survived')
ax[0].set_ylabel('')

data['Survived'].value_counts().plot(kind='bar', ax=ax[1])
# sns.countplot('Survived', data=data, ax=ax[1])
ax[1].set_title('Count plot - Survived')
plt.show()
