#!/usr/bin/python

from pycocotools.coco import COCO
import requests
import PIL
from io import BytesIO
from pathlib import Path
import os
import shutil


Path("dataset_source/coco/banana").mkdir(parents=True, exist_ok=True)
Path("dataset_source/coco/not_banana").mkdir(parents=True, exist_ok=True)
# Path("dataset/train/banana").mkdir(parents=True, exist_ok=True)
# Path("dataset/train/not_banana").mkdir(parents=True, exist_ok=True)
# Path("dataset/val/banana").mkdir(parents=True, exist_ok=True)
# Path("dataset/val/not_banana").mkdir(parents=True, exist_ok=True)

#####################################
# Get subset of data that has bananas
#####################################

# instantiate COCO specifying the annotations json path
coco = COCO('annotations/instances_train2014.json')
# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['banana'])
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)

print("Coco banana size:", len(images))

# Save the images into a local folder
num = 0
for im in images:
    # if num == 100:
    #     break
    # num += 1

    img_data = requests.get(im['coco_url']).content
    
    img_data = BytesIO(img_data)
    img_data = PIL.Image.open(img_data)
    # img_data = img_data.resize((96,96))
    img_data.save('dataset_source/coco/banana/' + im['file_name'])
    print(".", end="", flush=True)
print("", flush=True)


########################################
# Get subset of data that has no bananas
########################################
all_imgIds = coco.getImgIds()
all_images = coco.loadImgs(all_imgIds)

print("Coco total size:", len(all_images))

nb_images = []
for i in range(len(all_images)):
    if all_images[i] not in images:
        nb_images.append(all_images[i])

print("Coco not banana size:", len(nb_images))

# Save the images into a local folder
num = 0
for im in nb_images:
    # if num == len(images):
    #     break
    # num += 1
    
    img_data = requests.get(im['coco_url']).content
    
    img_data = BytesIO(img_data)
    img_data = PIL.Image.open(img_data)
    # img_data = img_data.resize((96,96))
    img_data.save('dataset_source/coco/not_banana/' + im['file_name'])
    print(".", end="", flush=True)
print("", flush=True)

print("Downloaded all Coco", len(nb_images))

# data = os.listdir("dataset/tmp/banana")
# train = data[: int(len(data) * .8)]
# val = data[int(len(data) * .8) : ]

# for name in train:
#     shutil.move(f"dataset/tmp/banana/{ name }", f"dataset/train/banana/")

# for name in val:
#     shutil.move(f"dataset/tmp/banana/{ name }", f"dataset/val/banana/")

# data = os.listdir("dataset/tmp/not_banana")
# train = data[: int(len(data) * .8)]
# val = data[int(len(data) * .8) : ]

# for name in train:
#     shutil.move(f"dataset/tmp/not_banana/{ name }", f"dataset/train/not_banana/")

# for name in val:
#     shutil.move(f"dataset/tmp/not_banana/{ name }", f"dataset/val/not_banana/")

# shutil.rmtree("dataset/tmp/")