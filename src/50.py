from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

for sex in ['male', 'female']:
    for pclass in range(1, 4):
        age_median = data[(data['Sex'] == sex) & (data['Pclass'] == pclass)]['Age'].median()
        data.loc[(data['Age'].isnull()) & (data['Sex'] == sex) & (data['Pclass'] == pclass), 'Age'] = age_median

data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data['Age'] = data['Age'].apply(lambda x: x // 10)


def fare2quantile(x):
    quantiles = [0.25, 0.5, 0.75]
    for i in range(len(quantiles)):
        if x < data['Fare'].quantile(quantiles[i]):
            return i
    else:
        return 3


data['Fare'] = data['Fare'].apply(fare2quantile)

data['FamilySize'] = data['SibSp'] + data['Parch']

data = data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked', 'SibSp', 'Parch'], axis=1)

print(data.columns)

X_train = data.drop('Survived', axis=1).values
target_label = data['Survived'].values

X_tr, X_vid, y_tr, y_vid = train_test_split(X_train, target_label, test_size=0.3, random_state=2018)

model = RandomForestClassifier()
model.fit(X_tr, y_tr)

pred = model.predict(X_vid)
print(pred)

acc = (pred == y_vid).sum() / X_vid.shape[0]

print('{:.2f}%'.format(acc * 100))
