# Recommendation System
Recommendation system is a system to predict the likelihood the audience would like a certain goods or services by predicting their rating or preference the audience would give. The major different recommendation system approachs are Collaborative Filtering, Content-based approach, and Hybrid model of both approaches. Collaborative filtering is a common machine learning algorithm to used to make the prediction. Here is the list of different kinds of collaborative filtering:
<ul>
	<li>Item-based Collaborative Filtering</li>
	<li>User-based Collaborative Filtering</li>
</ul>
<br>
Both Item-based and user-based collaborative filtering may use KNN and Correlation to determine the likelihood.

## Files
<ul>
	<li>cf_example.R</li>
	<li>cf_example.py</li>
</ul>

Note: The original author of <li>cf_example.R</li> is <a href="http://www.salemmarafi.com/code/collaborative-filtering-r/">Salem Marafi</a>

## Item-based Collaborative Filtering
Item-based collaborative filtering measures the similarity between an items that how much would the target audiences rate or like it. We may use KNN and Correlation to determine. In the case of using Cosine Correlation, we would use the following formula to calculate the correlation matrix:
<image src=Images/item_cf_formula.png>

### Example
<li>cf_example.R</li> is an example script obtained from Salem Marafi's blog post<a href="http://www.salemmarafi.com/code/collaborative-filtering-r/">Collaborative Filtering with R</a>
<br><br>
<i>cf_example.py</i> is an example script inspired from Salem Marafi's R script and translated to Python.
<br>
Coming Soon...

## User-based Collaborative Filtering
Coming Soon...


## Reference
Wikipedia: <a href="https://en.wikipedia.org/wiki/Collaborative_filtering">link</a><br>
Hackernoon: <a href="https://hackernoon.com/introduction-to-recommender-system-part-1-collaborative-filtering-singular-value-decomposition-44c9659c5e75">link</a><br>
Salem Marafi: <a href="http://www.salemmarafi.com/code/collaborative-filtering-r/">link</a><br>
Slide Share (KNN): <a href="https://www.slideshare.net/seydahatipoglu111/collaborative-filtering-using-knn">link</a><br>
Paper on Amazon.com Recommendations: <a href="http://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf
">link</a>