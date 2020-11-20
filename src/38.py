# 4살 이하에서 생존 확률이 매우 높다
# 최고령 승객은 살았다
# 15~25세 사이의 사람들은 죽은 사람이 많다
# 대부분의 승객은 15~35세다

# => 결론:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

print(data[['SibSp', 'Survived']].groupby(['SibSp']).mean().sort_values(by='Survived', ascending=False))

#        Survived
# SibSp
# 1      0.535885
# 2      0.464286
# 0      0.345395
# 3      0.250000
# 4      0.166667
# 5      0.000000
# 8      0.000000

# 적을수록 사망률 증가
