# Anomaly Detection
The goal of Anomaly Detection is to identify any rare event or item among a dataset. There are a lot of algorithms to achieve this goal. The purpose of this folder is to store all the exercises related to anomaly detection, and continuously adding more algorithm and scripts.

## Files
<ul>
	<li>tips_knn.py</li>
</ul>

## KNN
KNN is a supervised classification, the goal is to classify the observations within the dataset into k-groups through distance, such as Euclidean distance. Once the observations are classified, the next step is to obtain the average and set a threshold of outlier, usually the average plus 2 standard deviations. Finally, compare the observations with the threshold. If the observation is greater threshold, it is classified as outlier (or anomaly).

<br><br>
Example: <i>tips_knn.py</i>

## Isolation Forest
Coming soon...

## Reference
<a href="https://www.intellspot.com/anomaly-detection-algorithms/">5 Anomaly Detection Algorithms in Data Mining (With Comparison)</a>
<br><br>
<a href="https://youtu.be/RwmttGrJs08">Anomaly detection with KNN
</a>
<br><br>
<a href="https://en.wikipedia.org/wiki/Isolation_forest">Isolation Forest Wikipedia</a>
