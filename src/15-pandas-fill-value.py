import pandas as pd

data = pd.read_csv('../data/train.csv')

data['Age'] = data['Age'].fillna(data['Age'].median())
data['Cabin'] = data['Cabin'].fillna('N')
data['Embarked'] = data['Embarked'].fillna('S')

print(data.isnull().sum())
