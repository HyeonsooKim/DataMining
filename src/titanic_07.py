# https://www.kaggle.com/c/titanic/data
# 데이터 필터링 및 차트용 데이터로 가공

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

survived = data[data['Survived'] == 1]['Sex'].value_counts()
dead = data[data['Survived'] == 0]['Sex'].value_counts()

d1 = data[data['Survived'] == 1]['Sex'].value_counts()
d2 = data[data['Survived'] == 0]['Sex'].value_counts()
print(d1)
print(d2)
df = pd.DataFrame([d1, d2])
print(df)
df.index = ['Survived', 'Dead']
print(df)
