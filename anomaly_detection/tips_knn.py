import pandas as pd
import numpy as np
from pydataset import data
from sklearn.neighbors import NearestNeighbors
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Importing data
df = data('tips')
X = df[['total_bill', 'tip']]
# X = df[['total_bill', 'sex', 'size','smoker','tip', 'time']]

"""
# Converting categorical variables
X['is_male'] = pd.get_dummies(X['sex'])['Male']
X['is_smoker'] = pd.get_dummies(X['smoker'])['Yes']
X['is_dinner'] = pd.get_dummies(X['time'])['Dinner']

X = X[['total_bill','size','is_male','is_smoker','is_dinner','tip']]
"""

# Train model
model = NearestNeighbors(n_neighbors=2)
model.fit(X)

distances, indexes = model.kneighbors(X)

# distance will display an array of distance from each dimension
# eg -> [0. 1.10909873] means intercept and distance for tips dimension

print(model.kneighbors(X))
print(f"Distances are: {distances}")
print(f"{distances.mean(axis=1).mean(axis=0)}")
print(f"{distances.mean(axis=1).std(axis=0)}")
threshold = distances.mean(axis=1).mean(axis=0) + 2*(distances.mean(axis=1).std(axis=0))
print(threshold)
print(np.where(distances.mean(axis=1) > threshold))
print(f"{len(np.where(distances.mean(axis=1) > threshold)[0])} out of {df.shape[0]}")
print(np.where(distances.mean(axis=1) > threshold))

print(X.iloc[np.where(distances.mean(axis=1) > threshold)])
outliers = np.where(distances.mean(axis=1) > threshold)
inliers = np.where(distances.mean(axis=1) <= threshold)
print(X.iloc[outliers])


# Prepare Graph
data = []
data.append(go.Scatter(x=X.iloc[inliers]['total_bill'], y=X.iloc[inliers]['tip'],
              mode='markers', name='Inliers',
              line=dict(color='rgb(173,216,230)')))
data.append(go.Scatter(x=X.iloc[outliers]['total_bill'], y=X.iloc[outliers]['tip'],
              mode='markers', name='Outliers',
              line=dict(color='rgb(0,128,255)')))

# Prepare layout for stacked graph
layout = dict(title={'text':'Tips Dataset','x':0.5},
              xaxis=dict(title='Total Bill'), 
              yaxis=dict(title='Tips', gridcolor='lightgray'),
              legend=dict(x=0.1, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='tips_knn.html')
