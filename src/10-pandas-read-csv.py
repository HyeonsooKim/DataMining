# https://www.kaggle.com/c/titanic/data
# 데이터 로드 및 미리보기

import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.head())

#    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S
#
# [5 rows x 12 columns]
