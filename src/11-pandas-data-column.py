# https://www.kaggle.com/c/titanic/data
# 데이터 컬럼 분석

import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.columns)

# PassengerId: 승객 고유 ID
# Survived: 생존 여부 (0: 사망, 0: 생존)
# Pclass: 좌석 등급 (숫자가 낮을수록 좋은 등급)
# Name: 승객 이름
# Sex: 승객 성별
# Age: 승객 나이
# SibSp: 동승 형제/자매/배우자 수
# Parch: 동승 부모/자식 수
# Ticket: 티켓 번호
# Fare: 요금
# Cabin: 객실 번호
# Embarked: 정박 항구(C = Cherbourg, Q = Queenstown, S = Southampton)
