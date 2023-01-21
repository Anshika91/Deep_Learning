import numpy as np


class perceptron(object):
    def __init__(self,no_of_inputs,threshold=10,learning_rate=0.1):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs+1)
        
    def predict(self,inputs):
         summation = np.dot(inputs,self.weights[1:]) + self.weights[0]
         if summation > 0:
             return 1
         else:
              return 0

    def fit(self,training_inputs,label):
          for _ in range(self.threshold):
              for inputs,label in zip(training_inputs,label):
                  p=self.predict(inputs)
                  self.weights[1:]+= self.learning_rate*(label-p)*inputs
                  self.weights[0]+=  self.learning_rate*(label-p)

model = perceptron(3)
training_inputs = ([[0,0,0],[0,1,0],[1,0,0],[1,1,0],[1,0,1],[0,1,1],[0,0,1],[1,1,1]])
label = ([[0],[1],[1],[0],[],[],[],[]])
model.fit(training_inputs,label)

#test :
test = np.array([1,0,1])
print(model.predict(test))
