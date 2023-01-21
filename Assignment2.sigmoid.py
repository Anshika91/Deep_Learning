import numpy as np
import random

n=int(input("Enter the number of neurons in the hidden layer: "))

inputs=[]
num=int(input("Number of Inputs:"))
print("Enter the inputs:")
for i in range(0,num):
    x=int(input())
    inputs.append(x)

weights=[]
print("Enter the weights of hidden layer:")
for i in range(0,num*n):
    w=int(input())
    weights.append(w)


Weights=[]
print("Enter the weights of output layer:")
for i in range(0,n):
    W=int(input())
    Weights.append(W)

    

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate random input data
np.random.seed(51)
x = np.random.randn(10)

# Apply the sigmoid function to the input data
y = sigmoid(x)

print(y)



