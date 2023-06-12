# RandomSample Consensus (RANSAC)
An improved algorithm to encounter outliers in linear regression. When a dataset contains outliers (observation greater or less than 2 standard deviation from average), linear regression may not be robust enough. You may use this iterative and non-deterministic method to train the model when you try to take out the outlier influence in the model.
<br><br>
RANSAC uses voting scheme to find the optimal fitting result. There are two assumptions to this algorithm:
<ul>
	<li>Outliers do not influence the voting scheme consistently</li>
	<li>Ratio of inliners to outliers is sufficient to train the model (We don't have too many outliers)</li>
</ul>

## Algorithm
Before we started, you need to define the hyperparameter M and N, which represent how many observations are randomly selected in Step 1 and number of times the steps are going to be iterated.
<br><br>
Here are the steps:
<ul>
<li>Step 1: Select M points randomly from the dataset</li>
<li>Step 2: Train the model</li>
<li>Step 3: Check all the observation in the dataset and calculate the inliners to total number ratio. Verify if the ratio is within the Error Tolerance Threshold. If the ratio exceeds Minimum Valid Consensus Threshold, correct the parameters with the identified inliers and stop</li>
<li>Step 4: Repet Step 1-3 for N times</li>
</ul>


### How to Select N (How many times to be iterated)?
The probability of all points will be inliners in one iteration is <b>p = k^M</b>, where k is a probability of selected point is an inliner, in other words, (1-k) is the probability of a selected point is an outlier. After some derivation, N = log(1-p)/log(1-(1-k)^M)
<br><br>
The calculation would be:
<br><br>
<img src=iteration_required.png>
<br><br>
Note that the model would not work well if the proportion of outliers to be too large, and become not funcationable if it exceed 50%.


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
If the error tholerance threshold is too large, some outliers might be tolerance as liners. However, if the threshold is too small the optimal model might not able to be achieved. 

## Reference
The notes of this topic learnt from the following sources:
<br>
<b>Aknur Karaby</b> from the YouTube channel<b>ISSAI_NU</b>. YouTube video on<a href="https://youtu.be/SQB9GXxY6KY">Machine Learning Basics: Random Sample Consensus (RANSAC)</a>
<br><br>
YouTube channel <b>Educational Research Techniques</b>\'s video <a href="https://youtu.be/6lEPn1WkjVg">RANSAC Regression with Python</a>