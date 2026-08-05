import torch

### PATTERN 1: DIRECT CREATION FROM DATA
data = [[1,2,3],[4,5,6]]

my_tensor = torch.tensor(data)

print(my_tensor) #This output gives a tensor object that mirrors a list (two rows)
###