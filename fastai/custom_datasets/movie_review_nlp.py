from fastai.text.all import *
import torch

'''
fastai creates a learner with fresh pretrained AWD-LSTM 
weights and performs all the fine-tuning again. 
Each epoch must reread batches, calculate predictions, calculate gradients,
and update millions of parameters. 
Those calculations cannot simply be reused because 
they are the training process itself.
'''

device = torch.device("cpu")
print("Using:", device)

path = untar_data(URLs.IMDB)

dls = TextDataLoaders.from_folder(
    path,
    valid="test",
    num_workers=0,
    device=device
)

learn = text_classifier_learner(
    dls,
    AWD_LSTM,
    drop_mult=0.5,
    metrics=accuracy
)

learn.fine_tune(4, 1e-2)

#When the model finally gets done training...
learn.predict("I really liked that movie!") 



