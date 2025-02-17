model_influence = model.get_influence()
(c, _) = model_influence.cooks_distance

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

fig, ax = plt.subplots(figsize=(20, 7))  # Create fig and ax using subplots
plt.stem(np.arange(len(df)), np.round(c, 3))  # Use np.arange
plt.xlabel('Row Index')
plt.ylabel('Cooks Distance')
plt.show()

(np.argmax(c) , np.max(c))

from statsmodels.graphics.regressionplots import influence_plot
influence_plot(model)
plt.show()
k = df.shape[1]
n = df.shape[0]
leverage_cutoff = 3*((k + 1)/n)
df[df.index.isin([70, 76])]
df.head()