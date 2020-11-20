from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

data = data.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
data['Age'] = data['Age'].fillna(data['Age'].median())

X_train = data.drop('Survived', axis=1).values
target_label = data['Survived'].values

X_tr, X_vid, y_tr, y_vid = train_test_split(X_train, target_label, test_size=0.3, random_state=2018)

model = RandomForestClassifier()
model.fit(X_tr, y_tr)

pred = model.predict(X_vid)
print(pred)

acc = (pred == y_vid).sum() / X_tr.shape[0]

print('{:.2f}%'.format(acc * 100))
