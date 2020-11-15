# https://www.kaggle.com/c/titanic/data
# 여러가지 차트

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')
print(data['Cabin'])

data['Cabin'] = data['Cabin'].fillna('N')

data['Cabin'] = data['Cabin'].apply(lambda x: x[0])
print(data['Cabin'])

# data.plot(kind='box')
# data.plot(kind='line')
# data['Age'].fillna(data['Age'].median()).apply(lambda x: (int(x) // 10) * 10).value_counts().sort_index().plot(kind='bar', stacked=True)
# data['Age'].fillna(data['Age'].median()).apply(lambda x: (int(x) // 10) * 10).value_counts().sort_index().plot(kind='barh', stacked=True)
# data['Age'].fillna(data['Age'].median()).plot(kind='hist', bins=[i * 10 for i in range(0, 10)])
# data.plot(kind='hist')
# data['Fare'].plot(kind='kde')
# data.plot(kind='density')
# data['Cabin'].value_counts().plot(kind='pie')
# data['Age'].plot(kind='scatter')
# data.plot(kind='hexbin')

# data[data['Cabin'] != 'N']['Cabin'].value_counts().sort_index().plot(kind='bar')

survived = data[data['Survived'] == 1]['Sex'].value_counts()
dead = data[data['Survived'] == 0]['Sex'].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ['Survived', 'Dead']
df.plot(kind='bar', figsize=(10, 5))
plt.show()
