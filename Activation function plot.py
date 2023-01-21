import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))
def d_sig(x):
    return np.exp(-x)/((1+np.exp(-x))*(1+np.exp(-x)))

def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
def d_tanh(x):
    return (4*np.exp(-x)*np.exp(x))/(np.exp(x)+np.exp(-x))

def relu(x):
    return np.maximum(0,x)
    #d = map(lambda x:max(0,x),x)
    #return np.array(list(d))


x = np.linspace(-10,10)
plt.plot(x,sigmoid(x),'blue',label = 'sigmoid')
plt.plot(x,d_sig(x),'red',label='derivative of sigmoid')
plt.plot(x,tanh(x),'green',label = 'tanh')
plt.plot(x,d_tanh(x),'red',label = 'd_tanh')
plt.plot(x,relu(x),'purple',label = 'relu')
plt.legend()
plt.show()
