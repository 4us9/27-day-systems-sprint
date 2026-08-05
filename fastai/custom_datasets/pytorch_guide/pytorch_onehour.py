import torch
#In PyTorch, a tensor is a specialized, multi-dimensional array used 
# to store and manipulate model inputs, outputs, and parameters

def past_patterns():
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

    ### PATTERN 3: CREATION BY MIMICKING ANOTHER TENSOR
    #Sometimes need a tensor with same shape and type as another. So we MIMICK

    template = torch.tensor([[1,2],[3,4]])

    #notice the random is the exact replica as the template except different values
    rand_like = torch.randn_like(template, dtype=torch.float) 

    print(f"Template Tensor:\n {template}\n")
    print(f"Randn_like Tensor:\n {rand_like}")
    
    ###WHAT IS INSIDE A TENSOR?? Shape, type, and device
    # (You will be using these constantly for debugging) 
    tensor = torch.randn(2,3)
    print(f"Shape: {tensor.shape}") #tuple describing dimensions. THIS IS #1 DEBUGGING.
    print(f"Data type: {tensor.dtype}") #default is float32 for tensor. This is cause of gradients (the power of nudging). Weights and biases need to be float
    print(f"Device: {tensor.device}") #Where the tensors lives (CPU or GPU/CUDA)

    ### AUTOGRAD (Automatic Differentiation) -- PyTorch's built-in gradient calculator
    requires_grad = True #"The Magic Switch" Because tensor is just data, so you need it to be a learnable param
    #tells that it is a param, so track every operation that happens to this tensor.

    a = torch.tensor(2.0, requires_grad=True)
    b = torch.tensor(3.0, requires_grad=True)
    c = torch.tensor(4.0, requires_grad=True)

    ### THE "verbs" of PyTorch

    #Element wise: * (Multiplication) -- only works for the same shape

    #Element wise: @ (Powers neural networks -- matrix multiplication)
    #For linear layer of y = xW + b, you are always using the @. 
    m1 = torch.tensor([[1,2,3],[4,5,6]]) #(2,3)
    m2 = torch.tensor([[7,8,],[9,10],[11,12]]) # (3,2)

    matrix_product = m1@m2

    #DIM (where dim=0 calculates (by tensor.(data).mean(dim=#)) each vertical, and dim=1 calculates horizontal)
    #
    scores = torch.tensor([[10., 20., 30.], [5., 10., 15.]])
    avg_for_each_assignment = scores.mean(dim=0)
    avg_for_each_student = scores.mean(dim=1)

    print(avg_for_each_assignment)
    print(avg_for_each_student)


    ###INDEXING
    x = torch.arange(12).reshape(3,4)
    print(x)

    col_2 = x[:2,] #get the 3rd column (at index 2) -- gives all rows but only at index 2

    print(col_2)

    row_0 = x[0,:] #at row 0, give me all the columns


    ### DYNAMIC SELECTION: `ARGMAX` -- get largest

    ### gather -- more specific retrival of an element

### Forward Pass: Model's first guess
#Linear Regression: y(hat) = XW+b -- y (hat) is model prediction, x is the input, 'w' is weight, 'b' is bias
#Changes weights and bias to get as close to the prediction as possible.

##First Step - Creating Our Data
N = 10 #10 data points batch of data

#1 input feature & 1 output value
D_in = 1
D_out = 1

X = torch.randn(N,D_in)

print(X)

#True target labels
true_W = torch.tensor([[2.]]) #weights are vectors
true_b = torch.tensor(1.)

y_true = X @true_W + true_b + (torch.randn(N, D_out) * 0.1) # XW + b + (little noise)

#Initialize params (that it actually learn) and turn on the 'magic switch'
W = torch.randn(D_in, D_out, requires_grad=True)
b = torch.randn(1, requires_grad=True)

print(f"Initial Weight W:\n {W}\n")
print(f"Initial Bias b:\n {b}")

#Implementation from math to code
y_hat = X@W+b


#Our model prediction
print(f"Prediction y_hat (first three rows):\n {y_hat[:3]}\n") #terrible prediction BUT the Backward is doing its auto differentiation. The Periphery NS is working
print(f"Ture labels (first three rows):\n {y_true[:3]}\n")

#Loss function (MSE for linear regression)
error = y_hat - y_true
squared_error = error**2
loss = squared_error.mean()

print(f"Loss (our single scorecard number): {loss}") #MAKE THIS NUMBER AS SMALL AS POSSIBLE.


#Now, the `.grad` will tell us what knobs to adjust
#The gradients are stored in the .grad attributes
print(f"Gradient for W:\n {W.grad}\n")
print(f"Gradient for b:\n {b.grad}\n") #negative W/b means we need to increase to decrease the loss

##TRAINING LOOP (Gradient descent)
learning_rate, epochs = 0.01, 100 #n // hyperparameters

for epoch in range(epochs):                   
    #Forward pass and loss
    y_hat = X@W + b
    loss = torch.mean((y_hat-y_true)**2)
    
    #Backward pass
    loss.backward()
    
    #Update parms
    with torch.no_grad():
        W -= learning_rate * W.grad; b-= learning_rate * b.grad

    #Zero gradients -- get ready for next epoch
    W.grad.zero_(); b.grad.zero_()



#Repeat epoch 5 times
#`torch.no_grad()` this tells PyTorch to not track param updates in autograd
#`.grad.zero_()` -- set gradients after each iteration. If we didn't gradients would add on and gets really messy
