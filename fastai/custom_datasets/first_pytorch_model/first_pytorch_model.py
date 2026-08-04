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

device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print("Using device:", device)

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

train_folder ='/Users/pang/Documents/Coding/27-day-systems-sprint/fastai/custom_datasets/first_pytorch_model/data/archive/train'
valid_folder='/Users/pang/Documents/Coding/27-day-systems-sprint/fastai/custom_datasets/first_pytorch_model/data/archive/valid'
test_folder = '/Users/pang/Documents/Coding/27-day-systems-sprint/fastai/custom_datasets/first_pytorch_model/data/archive/test'

train_dataset=PlayingCardDataset(train_folder, transform)
val_dataset= PlayingCardDataset(valid_folder, transform=transform)
test_dataset = PlayingCardDataset(test_folder, transform=transform)

###Dataloader -- to parallize which PyTorch does for uss
train_loader=DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

#Iterate dataloader
for images, labels in train_loader:
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
        x=torch.flatten(x,1)
        
        output = self.classifier(x)
        return output


###Step 3: Training loop - used to train the model###
images = images.to(device)
labels = labels.to(device)

model = SimpleCardClassifier(num_classes=53).to(device)

example_output=model(images)


#Feed into model many times and perform loss function to the output received. 
#This is how the model learns. We do this in batches, hence DataLoader.

#optimizer & loss function
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print(criterion(example_output, labels)) #test to see if loss func. is working from images fed to training model

#TRAINING LOOP 5 EPOCH (5 runs of entire training set)
num_epoch = 5

train_losses = []
val_losses = []

for epoch in range(num_epoch):
    #Set model to train
    model.train()
    running_loss=0.0
    
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)
        
        optimizer.zero_grad()
        outputs=model(images)
        loss=criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss+=loss.item() * images.size(0)
    
    train_loss= running_loss / len(train_loader.dataset)
    train_losses.append(train_loss)
    
    #Validation phase
    model.eval()
    running_loss = 0.0
    
    #Ensure model weight not touched 
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            labels = labels.to(device)

            
            outputs=model(images)
            loss=criterion(outputs, labels)
            running_loss += loss.item() * images.size(0)
    
    val_loss=running_loss/len(val_loader.dataset)
    val_losses.append(val_loss)
        
    #Print epoch stats
    print(f"Epoch {epoch+1}/{num_epoch} - Train loss: {train_loss}, Validation loss: {val_loss}")    
    