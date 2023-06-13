import pandas as pd
import numpy as np
from pydataset import data
import plotly
import plotly.graph_objs as go
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)
# Importing data
df = data('tips')
X = df[['total_bill']]
y = df[['tip']]

# Prepare Graph for RANSAC
data = []
data.append(go.Scatter(x=X['total_bill'], y=y['tip'],
              mode='markers', name='Tips',
              line=dict(color='blue')))

# Prepare layout for stacked graph
layout = dict(title={'text':'Tips Dataset','x':0.5},
              xaxis=dict(title='Total Bill'), 
              yaxis=dict(title='Tips', gridcolor='lightgray'),
              legend=dict(x=0.1, y=1, orientation='h'),
              plot_bgcolor='rgba(0,0,0,0)')

# Plot and fix layout
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='tips_eda.html')
