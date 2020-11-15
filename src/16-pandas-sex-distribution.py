# https://www.kaggle.com/c/titanic/data
# 데이터 분포 시각화

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

sex_count = data['Sex'].value_counts()
df = pd.DataFrame([sex_count])
df.index = ['Total']
print(df)
df.plot(kind='bar')
plt.show()

#      male  female
# Sex   577     314
#
# Process finished with exit code 0
