from fastai.vision.all import * 

#The segmentation model used from fastAI of the CamVid dataset
#The Paper: Semantic Object Classes in Video: A High Definition Ground Truth DB

path = untar_data(URLs.CAMVID_TINY)
dls = SegmentationDataLoaders.from_label_func(
    path, bs=8, fnames=get_image_files(path/'images'),
    label_func = lambda o: path/'labels'/f'{o.stem}_P{o.suffix}',
    codes=np.loadtxt(path/'codes.txt', dtype=str)
)
