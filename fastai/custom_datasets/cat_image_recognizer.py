#gives all the func and classes we will need
### Classifying Cats ###

#to create a wide variety of computer vision models
from fastai.vision.all import * 


#downloading dataset specifically from fastai
path = untar_data(URLs.PETS)/'images'

'''
is_cat function based on filename rule provided
by the dataset's creators
'''
def is_cat(x):
    return x[0].isupper()

#tells what kind of data set we use and how it is structured
#get data from path, telling the y is is_cat
#seed of 42 means same vallue every time we run the code; to get same valid set
dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2,
    seed=42, label_func=is_cat, item_tfms=Resize(224)
)

#Create a CNN as well as the architecture we are using (the model type).
#34 means 34 layers
#metric is the feedback--error or accuracy
#pretrained is set to True to make our model more accurate models
learn = cnn_learner(dls, resnet34, metrics=error_rate) 

learn.fine_tune(1)

