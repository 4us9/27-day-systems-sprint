#First model implemented using a PyTorch library

#Problem to solve: take image and detect which card is in that img

#Three main paradigms to train a PyTorch model: datasets & loader, PyTorch model module, PyTorch training loop

import pytorch 
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import timm 
import matplotlib.pyplot as plt #for data visualization
import pandas as pd
import numpy as np
