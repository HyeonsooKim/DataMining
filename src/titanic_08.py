# https://www.kaggle.com/c/titanic/data
# 데이터 탐색 전에 결측값을 치환한다.
# fillna 함수로 결측값에 넣을 값을 지정
# Age의 경우 중앙값으로 채우기

import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.isnull().sum())

data['Age'] = data['Age'].fillna = data['Age'].median()
print(data.isnull().sum())
