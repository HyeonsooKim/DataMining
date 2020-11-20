# 1. 여성이 더 많이 생존 (18)
# 2. 1등급 좌석의 사람들이 더 많이 생존 (24)


# 2번 좌석별 생존 확률

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

print(data[['Pclass', 'Survived']].groupby(['Pclass']).mean().sort_values(by='Survived', ascending=False))

#         Survived
# Pclass
# 1       0.629630
# 2       0.472826
# 3       0.242363

# 1등급 좌석이 생존확률이 제일 높고
# 등급이 높을 수록 생존 확률이 높다
