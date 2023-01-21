import numpy as np
from sklearn.datasets import load_iris
iris=load_iris()

def pred(x,w):
    return 1 if(x*w).sum()>2 else 0
x=iris.data[:,(2,3)]
y=(iris.target==0).astype(np.int64)

def learning(x,y,w):
    print('weights:',w)
    for k in range(300):
        print('iteration:',k+1)
        for i,j in zip(x,y):
            if j-pred(i,w)>0:
                w= w+0.01*i
            elif j-pred(i,w)<0:
                w=w-0.01*i
            else:
                a=1
    return w


np.random.seed(2)
#np.random.seed(1)#for 100% accuracy use this.
x=np.array([[0,0,0],[0,1,0],[1,0,0],[1,1,0],[1,0,1],[0,1,1],[0,0,1],[1,1,1]])
y=np.array([[0],[0],[0],[0],[0],[0],[0],[1]])
w=np.random.randn(len(x[0]))
#w=[0.81324215, 1.17373317, 0.0138039 ] known as Transfer learning.
w=learning(x,y,w)
print('weights are :',w)
print('output is:',y)

#test
#print('test instance 1:',pred(x[1],w)==y[1])
#print('test instance 10:',pred(x[10],w)==y[10])
#print('test instance -1:',pred(x[-1],w)==y[-1])


#Accuracy
correct,incorrect=0,0
for i,j in zip(x,y):
    if pred(np.array(i),w)==j:
        correct+=1
    else:
        incorrect+=1
accuracy=(1.0* correct)/len(x)
print('accuracy is :',accuracy*100,'%')


#working for both gates And and OR


