import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# read in data
data_post = pd.read_csv('clem_zfish_postsynapses.csv')
data_pre = pd.read_csv('clem_zfish_presynapses.csv')

# create the 3d figure
fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111, projection='3d')

# filter data so you only keep those that are marked "valid"
valid_pre = data_pre[data_pre.iloc[:, 7].astype(str).str.strip() == "valid"]
valid_post = data_post[data_post.iloc[:, 7].astype(str).str.strip() == "valid"]

#plot; the color red is for the presynapses, and blue for the post synapses; added alpha to remove the varying transparencies
ax.scatter(valid_pre.iloc[:, 1], valid_pre.iloc[:, 2], valid_pre.iloc[:, 3], s=valid_pre.iloc[:, 5], c="red", alpha = 1)

ax.scatter(valid_post.iloc[:, 1], valid_post.iloc[:, 2], valid_post.iloc[:, 3], s=valid_post.iloc[:, 5], c="blue", alpha = 1)

# labeling the axes
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')

# showing the graph
plt.show()





