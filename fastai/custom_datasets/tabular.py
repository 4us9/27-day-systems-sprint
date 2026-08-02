from fastai.tabular.all import * 

path = untar_data(URLs.ADULT_SAMPLE) 
dls = TabularDataLoaders.from_csv(path/'adult.csv', path=path, y_names="salary",
    cat_names = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race'],     
    cont_names = ['age', 'fnlwgt', 'education-num'],
    procs = [Categorify, FillMissing, Normalize])

learn = tabular_learner(dls, metrics=accuracy) 

#since we are not using a pretrained model, we do not finetune. We instead fit_one_cycle (used for from scratch models)
learn.fit_one_cycle(3) 
