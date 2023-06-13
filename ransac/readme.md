# Random Sample Consensus (RANSAC)
An improved algorithm to encounter outliers in linear regression. When a dataset contains outliers (observation greater or less than 2 standard deviation from average), linear regression may not be robust enough. You may use this iterative and non-deterministic method to train the model when you try to take out the outlier influence in the model.
<br><br>
RANSAC uses voting scheme to find the optimal fitting result. There are two assumptions to this algorithm:
<ul>
	<li>Outliers do not influence the voting scheme consistently</li>
	<li>Ratio of inliners to outliers is sufficient to train the model (We don't have too many outliers)</li>
</ul>

## Algorithm
Before we started, you need to define the hyperparameters M and N, which represent how many observations are randomly selected in Step 1 and the number of times the steps are going to be iterated.
<br><br>
Here are the steps:
<ul>
<li>Step 1: Select M points randomly from the dataset</li>
<li>Step 2: Train the model</li>
<li>Step 3: Check all the observations in the dataset and calculate the inliners to total number ratio. Verify if the ratio is within the Error Tolerance Threshold. If the ratio exceeds Minimum Valid Consensus Threshold, correct the parameters with the identified inliers and stop</li>
<li>Step 4: Repeat Steps 1-3 for N times</li>
</ul>


### How to Select N (How many times to be iterated)?
The probability of all points will be inliners in one iteration is <b>p = k^M</b>, where k is a probability of the selected point is an inliner, in other words, (1-k) is the probability of a selected point is an outlier. After some derivation, N = log(1-p)/log(1-(1-k)^M)
<br><br>
The calculation would be:
<br><br>
<img src=images/iteration_required.png>
<br><br>
Note that the model would not work well if the proportion of outliers is too large, and become not funcationable if it exceeds 50%.


## Advantage
<ul>
	<li>Easy to implement</li>
	<li>Applicable to large datasets</li>
	<li>Handle outliers very well</li>
</ul>

## Disadvantage
<ul>
	<li>Tuning is very hard and time consuming</li>
	<li>Finding a reasonable inlier to outlier ratio is hard (Should be greater than 50%)</li>
</ul>

<br><br>
If the error tolerance threshold is too large, some outliers might be tolerance as liners. However, if the threshold is too small the optimal model might not be able to be achieved. 

## Example - Tips Dataset from PyDataset
<img src=images/tips_dataset.png>
<img src=images/tips_lr.png>
<img src=images/tips_ransac.png>
<br>
Linear Regression R2: 0.4687		vs 		Ransac R2: 0.4298
Linear Regression MAE: 0.7368	vs 			Ransac MAE: 0.7649
<br><br>
See the Script section for explanation.
<br><br>
When you compare the visualizations between two algorthms, you may able to find the RANSAC model is able to identify the outliers - The outliers are further away from the prediction line. Even the R-square of RANSAC model is lower, but the MAE is higher, which means the fit in RANSAC model is closer to the median. As the R-square formula is more sensitive to outliers penalties, we may use MAE to evaluate the accuracy between two models. We can see the MAE of RANSAC model is greater than Linear Regression model, it means the accuracy of RANSAC model is better while minimizing the influence from the outliers in the dataset.
<br><br>
The script sets the random state of RANSAC to 0. If the seed is set differently, the MAE will be different since the algorithm randomly selects the subset of data for calculation.
<br><br>
Note: If there are many outliers then you may consider using Mean Absolute Error (MAE). RMSE (R-square) is more sensitive to outliers than the MAE. But when outliers are exponentially rare (like in a bell-shaped curve), the RMSE performs very well and is generally preferred.
<br>
Source: <a href="https://stats.stackexchange.com/a/486577">StackExchange post</a>

## Script
The <i>Tips</i> dataset from PyDataset, it contains columns like total_bill (Bill total amount, in float), sex (Male or Female), size (Party size, in integer), smoker (Yes or No), time (Lunch or Dinner), and Tips (Tips paid, in float).

### eda_tips.py
The script downloads the <i>Tips</i> dataset from PyDataset and visualize the dataset with Plotly.

### tips.py
The script first download the <i>Tips</i> dataset from PyDataset. The first step is to convert text data into categorical variable, including sex, smoker, and time. Since the columns are only have two values, so it is easy to convert the columns to just one categorical value per columns.
<br>
Then, we would train the model with linear regression and RANSAC. After training the model with RANSAC, we would use the <i>.inlier_mask_</i> attribute to identify whether each data point is inliner or outlier, which would be use for visualization. 
<br>
And finally visualize the results from both algorithm with Plotly. The metrics of both algorithms also are printed on command line as well.

## Reference
RANSAC on <a href="https://en.wikipedia.org/wiki/Random_sample_consensus">Wikipedia</a>
<br><br>
The notes of this topic learnt from the following sources:
<br>
1. <b>Aknur Karaby</b> from the YouTube channel<b>ISSAI_NU</b>. YouTube video on <a href="https://youtu.be/SQB9GXxY6KY">Machine Learning Basics: Random Sample Consensus (RANSAC)</a>
2. YouTube channel <b>Educational Research Techniques</b>\'s video <a href="https://youtu.be/6lEPn1WkjVg">RANSAC Regression with Python</a>
3. StackExchange post <a href="https://stats.stackexchange.com/questions/48267/mean-absolute-error-or-root-mean-squared-error">Mean absolute error OR root mean squared error?</a>
