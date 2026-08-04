#First model implemented using a PyTorch library

#Problem to solve: take image and detect which card is in that img

#Three main paradigms to train a PyTorch model: datasets & loader, PyTorch model module, PyTorch training loop

import torch 
import torch.nn as nn #neural networks
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import timm #loading archictecture for image classifications
import matplotlib.pyplot as plt #for data visualization
import pandas as pd
import numpy as np

###Step 1: set up Dataset###
class PlayingCardDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data = ImageFolder(data_dir, transform=transform)
    
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx): #spcial method for indexing
        return self.data[idx]
    
    @property
    def classes(self):
        return self.data.classes 
    

#transforming data to be the same size as model expects it

transform = transforms.Compose([
    
    transforms.Resize([128,128]),
    transforms.ToTensor(),
])

data='/Users/pang/Documents/Coding/27-day-systems-sprint/fastai/custom_datasets/first_pytorch_model/data/archive/train'
    
dataset=PlayingCardDataset(data, transform)

###Dataloader -- to parallize which PyTorch does for uss
dataloader=DataLoader(dataset, batch_size=32, shuffle=True)

#Iterate dataloader
for images, labels in dataloader:
    break

print(images.shape)

###Step 2: PyTorch model###
#State-of-art pre-trained models from timm
class SimpleCardClassifier(nn.Module):
    def __init__(self, num_classes=53):
        super(SimpleCardClassifier, self).__init__()
        
        #Where we define all the parts of the model
        self.base_model= timm.create_model('efficientnet_b0', pretrained=True)
        self.features=nn.Sequential(*list(self.base_model.children())[:-1])
        
        enet_out_size=1280
        
        #Make a classifier
        self.classifier=nn.Linear(enet_out_size, num_classes)
        
    def forward(self, x):
        #Connect these parts and return the output
        x=self.features(x)
        output = self.classifier(x)
        
        return output

model=SimpleCardClassifier(num_classes=53)

print(model)