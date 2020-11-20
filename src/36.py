# 친척 수에 따른 사망율

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
