# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:45:58 2017

@author: mouni
"""

import numpy as np
import pickle 
class ANN:

  
        def build(self):
            self.b_inputneurons=8
            self.b_outputneurons=8
            self.hidden_neurons = 3 #number of hidden layers neurons
            self.wh=np.random.uniform(size=(self.b_inputneurons,self.hidden_neurons))
            self.bh=np.random.uniform(size=(1,self.hidden_neurons))
            self.wout=np.random.uniform(size=(self.hidden_neurons,self.b_outputneurons))
            self.bout=np.random.uniform(size=(1,self.b_outputneurons))
        #Sigmoid Function
        def sigmoid(self,x):
            return 1/(1 + np.exp(-x))
        
        #Derivative of Sigmoid Function
        def derivatives_sigmoid(self,x):
            return x * (1 - x)
        
        def train(self,iter):
            self.learnrate=0.33
            for i in range(iter):
                self.fwd_prop(self.A)
                self.back_prop()
        def fit(self,input_neuron):
            self.input_neuron=input_neuron
            return self.fwd_prop(self.input_neuron)
        
       

        def fwd_prop(self,input_val):
            self.hidden_layer_input1=np.dot(input_val,self.wh)
            
            self.hidden_layer_input=self.hidden_layer_input1 + self.bh
            self.hiddenlayer_activations = self.sigmoid(self.hidden_layer_input)
            self.output_layer_input1=np.dot(self.hiddenlayer_activations,self.wout)
            self.output_layer_input= self.output_layer_input1+ self.bout
            self.output = self.sigmoid(self.output_layer_input)
          
            return self.output
            
        
        def back_prop(self):
            E = self.B-self.output
            slope_output_layer = self.derivatives_sigmoid(self.output)
            slope_hidden_layer = self.derivatives_sigmoid(self.hiddenlayer_activations)
            d_output = E * slope_output_layer
            Error_at_hidden_layer = d_output.dot(self.wout.T)
            d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer
            self.wout += self.hiddenlayer_activations.T.dot(d_output) *self.learnrate
            self.bout += np.sum(d_output, axis=0,keepdims=True) *self.learnrate
            self.wh += self.A.T.dot(d_hiddenlayer) *self.learnrate
            self.bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *self.learnrate
        
        def save(self):
            with open('output.txt', 'wb') as final_output:
                pickle.dump(self,final_output)
        
        def restore(self):
            with open('output.txt','rb') as f:
                return pickle.load(f)
        
     
          #Input array
        A=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]])
    
    #Output array
        B=np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],
                [0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]])
a=ANN()
a.build()
a.train(660)
b= np.array([1,0,0,0,0,0,0,0])
print(a.fit(b))
a.save()
a.restore()