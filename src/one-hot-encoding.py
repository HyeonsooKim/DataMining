import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data['Embarked'] = data['Embarked'].fillna('S')
data['Embarked'] = data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
# print(data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).unique())

# print(data.groupby('Embarked').sum())

print(data.columns)

print(data[data['Pclass'] == 1]['Cabin'].isnull().sum())

data.loc[(data['Pclass'] == 1) & (data['Cabin'].isnull()), 'Cabin'] = 'A'

print(data[data['Pclass'] == 1]['Cabin'].isnull().sum())

# data = pd.get_dummies(data, columns=['Embarked'], prefix='Embarked')

# print(data)
