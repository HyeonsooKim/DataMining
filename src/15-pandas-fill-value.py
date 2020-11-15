# https://www.kaggle.com/c/titanic/data
# 결측값(null) 채우기

import pandas as pd

data = pd.read_csv('../data/train.csv')

data['Age'] = data['Age'].fillna(data['Age'].median())
data['Cabin'] = data['Cabin'].fillna('N')
data['Embarked'] = data['Embarked'].fillna('S')

print(data.isnull().sum())

# PassengerId    0
# Survived       0
# Pclass         0
# Name           0
# Sex            0
# Age            0
# SibSp          0
# Parch          0
# Ticket         0
# Fare           0
# Cabin          0
# Embarked       0
# dtype: int64
#
# Process finished with exit code 0
