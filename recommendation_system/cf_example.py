import numpy as np
import pandas as pd


# Function to 
def cos_similarity(x,y):
    sum_x2 = np.sum(np.square(x))
    sum_y2 = np.sum(np.square(y))
    sum_xy = np.sum([x*y for x,y in zip(x,y)])
    return sum_xy/np.sqrt(sum_x2*sum_y2)

# Read data and get the list of singers available
df_lastfm = pd.read_csv('../Data/lastfm-matrix-germany.csv')
singers = df_lastfm.drop('user', axis=1).columns

# Loop over each singer and find 
similarity_singers = []
for i in singers:
	temp = []
	for j in singers:
		temp.append(cos_similarity(df_lastfm[i],df_lastfm[j]))
	similarity_singers.append(temp)

similarity_singers = pd.DataFrame(similarity_singers, columns=singers)
similarity_singers['singers'] = singers
similarity_singers = similarity_singers[['singers']+singers.tolist()]
similarity_singers.to_csv('result.csv', index=False)
