# 1. 여성이 더 많이 생존 (18)
# 2. 1등급 좌석의 사람들이 더 많이 생존 (24)


# 1번 여성이 더 많이 생존

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/train.csv')

print(data[['Sex', 'Survived']].groupby(['Sex']).mean().sort_values(by='Survived', ascending=False))

#        Survived
# Sex
# female  0.742038
# male    0.188908

# 여자 생존율이 상당히 높음
