import numpy as np
import json
import torch
import torch.nn as nn
from torch.utils.data import dataset,dataloader
from NeuralNetwork import bag_of_words , tokenize , stem
from brain import NeuralNet

with open('intents.json','r') as f:
    intents = json.load(f)
    
all_words = []
tags = []
x = []
y = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    
    
    
          
