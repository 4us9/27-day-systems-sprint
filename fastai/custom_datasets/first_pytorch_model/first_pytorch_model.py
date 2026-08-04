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

#Step 1: set up Dataset
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
    

dataset = PlayingCardDataset(
    data_dir='/Users/pang/Documents/Coding/27-day-systems-sprint/fastai/custom_datasets/first_pytorch_model/data'
)
    
print(len(dataset))

print(dataset[0])