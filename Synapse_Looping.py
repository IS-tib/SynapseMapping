import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_post = pd.read_csv('clem_zfish_postsynapses.csv')
data_pre = pd.read_csv('clem_zfish_presynapses.csv')

fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(data_pre)):
    if (str(data_pre.iloc[i, 7]).strip() == "valid"):
        x = data_pre.iloc[i, 1]
        y = data_pre.iloc[i, 2]
        z = data_pre.iloc[i, 3]
        size = data_pre.iloc[i, 5]
        ax.scatter(x, y, z, s = size,c = "red")

for i in range(len(data_post)):
    if (str(data_post.iloc[i, 7]).strip() == "valid"):
        x = data_post.iloc[i, 1]
        y = data_post.iloc[i, 2]
        z = data_post.iloc[i, 3]
        size = data_post.iloc[i, 5]
        ax.scatter(x, y, z, s = size, c = "blue")

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()





