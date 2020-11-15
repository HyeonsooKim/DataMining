# https://www.kaggle.com/c/titanic/data
# 결측값(null) 분포 확인

import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.isnull().sum())

# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
# dtype: int64
#
# Process finished with exit code 0

