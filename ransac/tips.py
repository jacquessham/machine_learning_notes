import math
import pandas as pd
import numpy as np
from pydataset import data
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.metrics import r2_score
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# The code is replicating from Educational Research Techniques
# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Importing data
df = data('tips')
X = df[['total_bill', 'sex', 'size','smoker','time']]
y = df[['tip']]
# Converting categorical variables
X['is_male'] = pd.get_dummies(X['sex'])['Male']
X['is_smoker'] = pd.get_dummies(X['smoker'])['Yes']
X['is_dinner'] = pd.get_dummies(X['time'])['Dinner']
# Drop the text data
X = X[['total_bill','size','is_male','is_smoker','is_dinner']]

# Train Linear Regression
model_lr = LinearRegression()
model_lr.fit(X, y)
pred_lr = model_lr.predict(X)

r2_lr = r2_score(y, pred_lr)

# Train RANSAC
model_ransac = RANSACRegressor(LinearRegression(), residual_threshold=2, random_state=0)
model_ransac.fit(X, y)
pred_ransac = model_ransac.predict(X)

r2_ransac = r2_score(y, pred_ransac)

# Print result
print('LinearRegression: '+str(r2_lr))
print('Ransac: '+str(r2_ransac))

# Prepare a line
pt_line = np.arange(0,math.ceil(y.max())+1,1)

inliers = model_ransac.inlier_mask_
outliers = np.logical_not(inliers)


# Prepare Graph for RANSAC
data = []
data.append(go.Scatter(x=y[inliers]['tip'], y=pred_ransac.ravel()[inliers],
              mode='markers', name='Inliers',
              line=dict(color='rgb(173,216,230)')))
data.append(go.Scatter(x=y[outliers]['tip'], y=pred_ransac.ravel()[outliers],
              mode='markers', name='Outliers',
              line=dict(color='rgb(0,128,255)')))
data.append(go.Scatter(x=pt_line, y=pt_line,
              mode='lines', name='Prediction',
              line=dict(color='red')))

# Prepare layout for stacked graph
layout = dict(title={'text':'Tips (RANSAC)','x':0.5},
              xaxis=dict(title='Actual Tips'), 
              yaxis=dict(title='Predicted Tips', gridcolor='lightgray'),
              legend=dict(x=0.1, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='tips_ransac.html')

# Prepare Graph for LR
data = []
data.append(go.Scatter(x=y[inliers]['tip'], y=pred_lr.ravel(),
              mode='markers', name='Inliers',
              line=dict(color='rgb(173,216,230)')))
data.append(go.Scatter(x=y[outliers]['tip'], y=pred_lr.ravel()[outliers],
              mode='markers', name='Outliers',
              line=dict(color='rgb(0,128,255)')))
data.append(go.Scatter(x=pt_line, y=pt_line,
              mode='lines', name='Prediction',
              line=dict(color='red')))

# Prepare layout for stacked graph
layout = dict(title={'text':'Tips (Linear Regression)','x':0.5},
              xaxis=dict(title='Actual Tips'), 
              yaxis=dict(title='Predicted Tips', gridcolor='lightgray'),
              legend=dict(x=0.1, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='tips_lr.html')
