from fastai.text.all import *
import torch

device = torch.device(
    "mps" if torch.backends.mps.is_available() else "cpu"
)

print("Using:", device)

path = untar_data(URLs.IMDB)

dls = TextDataLoaders.from_folder(
    path,
    valid="test",
    device=device,
    num_workers=0
)

learn = text_classifier_learner(
    dls,
    AWD_LSTM,
    drop_mult=0.5,
    metrics=accuracy
)

learn.fine_tune(4, 1e-2)