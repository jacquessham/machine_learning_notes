import numpy as np
import pandas as pd


# Function to 
def cos_similarity(x,y):
    sum_x2 = np.sum(np.square(x))
    sum_y2 = np.sum(np.square(y))
    sum_xy = np.sum([x*y for x,y in zip(x,y)])
    return sum_xy/np.sqrt(sum_x2*sum_y2)

# Read data and get the list of singers available
print('Reading dataset...')
df_lastfm = pd.read_csv('../Data/lastfm-matrix-germany.csv')
singers = df_lastfm.drop('user', axis=1).columns

# Gather parameters
save_matrix = True
save_result = True
num_recommend = 10

# Loop over each singer and find
print('Calculating similarity scores...')
similarity_singers = []
for i in singers:
	temp = []
	for j in singers:
		temp.append(cos_similarity(df_lastfm[i],df_lastfm[j]))
	similarity_singers.append(temp)

# Re-frame it into Pandas DataFrame
print('Preparing the Similarity Matrix...')
similarity_singers = pd.DataFrame(similarity_singers, columns=singers)
# Add column of singers to make it matrix-like to save
similarity_singers['singers'] = singers
# Rearrange columns order
similarity_singers = similarity_singers[['singers']+singers.tolist()]
print('Similarity Matrix Prepared!')
# Save matrix to csv
if save_matrix:
	print('Saving Similarity Matrix...')
	similarity_singers.to_csv('Results/item_cf_similarity_matrix.csv', index=False)
	print('Similarity Matrix sucessfully saved!')


# Convert similarity to recommendation (Number convert to singer names)
def convert_name(df, col_singers, col_score, top_n):
	df = df.sort_values(col_score).head(top_n+1)
	col_result = df[col_singers].iloc[1:].tolist()
	return col_result

print('Converting Similarity Matrix to result...')
result = {}
for col in similarity_singers.columns:
	if col != 'singers':
		result[col] = convert_name(similarity_singers, 'singers',
			                       col, num_recommend)
result = pd.DataFrame(result)
print('Result Prepared!')
if save_result:
	print('Saving result...')
	result.to_csv('Results/it_cf_result.csv', index=False)
	print('Result successfully saved!')

