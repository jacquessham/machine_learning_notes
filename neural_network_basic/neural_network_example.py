import numpy as np
import os
from random import random

# Learning Rate
lr = 1
bias = 1

# Weights for 2 neurons and bias, randonly picked between 0 and 1
weights = [random() for _ in range(3)]

print(weights)

# The goal is to adjust weights through learning from the training data
def perceptron(input1, input2, label):
	outputP = input1*weights[0] + input2*weights[1] + bias*weights[2]
	if outputP > 0:
		outputP = 1
	else:
		outputP = 0

	error = label - outputP

	# Update the weights based on the prediction and error
	weights[0] = error*input1*lr
	weights[1] = error*input2*lr
	weights[2] = error*bias*lr 
	# print(f'{input1} or {input2} is: {outputP}')
	return outputP

# Training Phase
for i in range(1):
	perceptron(1,1,1) # True or True
	perceptron(1,0,1) # True or False
	perceptron(0,1,1) # False or True
	perceptron(0,0,0) # False or False

# Evaluation Phase
currP = perceptron(0,0,0)
result = 1/(1+np.exp(-currP))

print(f"The probability of True is {result}")
