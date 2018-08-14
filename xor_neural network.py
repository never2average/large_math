# -*- coding: utf-8 -*-
import numpy as np
import random
__author__="Priyesh Srivastava"
#print(__author__)

"""
Creating the neural network for an xor gate trained by back propogation
"""
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return x*(1-x)

class neuralnetwork:
    def __init__(self,inputs):
        random.seed(1)
        '''seed the random number to make sure that the same random number is used
    for all the testcases
        '''
        self.inputs=inputs
        self.l=len(inputs)
        self.li=len(inputs[0])
        
        self.wi=np.random.random((self.li,self.l)) # weight for the initial layer
        
        self.wh=np.random.random((self.l,1)) #weight for the hidden layer
        
    def think(self,inp):
        s1=sigmoid(np.dot(inp,self.wi))
        s2=sigmoid(np.dot(s1,self.wh))
        return s2
    
    def train(self,inputs,outputs,it):

        for i in range(it):
            l0=inputs
            l1=sigmoid(np.dot(l0,self.wi))
            l2=sigmoid(np.dot(l1,self.wh))
            
            l2_err=outputs-l2
            l2_delta=np.multiply(l2_err,sigmoid_der(l2))
            
            l1_err=np.dot(l2_delta,self.wh.T)
            l1_delta=np.multiply(l1_err,sigmoid_der(l1))
            
            self.wh+=np.dot(l1.T,l2_delta)
            self.wi+=np.dot(l0.T,l1_delta)
            

inputs=np.array([[0,0],[0,1],[1,0],[1,1]])
outputs=np.array([[0],[1],[1],[0]])

n=neuralnetwork(inputs)
print('before training')
print (n.think(inputs))

n.train(inputs,outputs,100000)

print('after training')
print (n.think(inputs))

      
    
            
            
        
    
