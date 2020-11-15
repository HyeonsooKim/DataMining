# https://www.kaggle.com/c/titanic/data
# 생존/사망 승객의 남/여 비율 데이터 시각화

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')
print(data.isnull().sum())

survived = data[data['Survived'] == 1]['Sex'].value_counts()
dead = data[data['Survived'] == 0]['Sex'].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ['Survived', 'Dead']
df.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.show()
