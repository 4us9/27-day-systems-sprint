import torch
#In PyTorch, a tensor is a specialized, multi-dimensional array used 
# to store and manipulate model inputs, outputs, and parameters

### PATTERN 1: DIRECT CREATION FROM DATA
data = [[1,2,3],[4,5,6]]

my_tensor = torch.tensor(data)

print(my_tensor) #This output gives a tensor object that mirrors a list (two rows)
###

### PATTERN 2: CREATION FROM DESIRED SHAPE
# Using it when initializing model weights
# Know shape you need, but not the values yet    

shape = (2,3) #tuple of two rows and three columns
ones = torch.ones(shape)
zeros= torch.zeros(shape)
random = torch.randn(shape)

print(f"Random Tensor:\n {random}")
print(f"Zero Tensor:\n {zeros}")
print(f"Zero Tensor:\n {ones}")

