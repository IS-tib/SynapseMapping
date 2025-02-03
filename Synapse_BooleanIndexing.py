import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data_post = pd.read_csv('clem_zfish_postsynapses.csv')
data_pre = pd.read_csv('clem_zfish_presynapses.csv')

fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111, projection='3d')

valid_pre = data_pre[data_pre.iloc[:, 7].astype(str).str.strip() == "valid"]
valid_post = data_post[data_post.iloc[:, 7].astype(str).str.strip() == "valid"]

ax.scatter(valid_pre.iloc[:, 1], valid_pre.iloc[:, 2], valid_pre.iloc[:, 3], s=valid_pre.iloc[:, 5], c="red")

ax.scatter(valid_post.iloc[:, 1], valid_post.iloc[:, 2], valid_post.iloc[:, 3], s=valid_post.iloc[:, 5], c="blue")

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()





