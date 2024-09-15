# My CV helper tools

A collection of my personal helper tools and scripts for working with images, files and folders in CV tasks.

## dataset_split.ipynb

Split folders with files (e.g. images) into train, validation and test (dataset) folders.

see: [split-folders](https://github.com/jfilter/split-folders)

default: train 80%, val 10%, test 10%

## merge_subfolder_images.ipynb

Merge all images from a folder and its subfolders into a single folder. Recombine split images in subfolder structures

## resize_images.ipynb

Resize images to a new target resolution. Works with a folder with subfolders.

## duplicate_images.ipynb

Duplicate an image by the specified factor.

## delete_random_images.py

Delete random images from a folder. Specify a number of images to be left.

## Ms PowerToys PowerRename

Rename all files. see: https://learn.microsoft.com/de-de/windows/powertoys/powerrename

Note: Activate RegEx

```
(.*).jpeg

name_${padding=4;increment=1;start=1}

```

## Requirements

```
split-folders
ipykernel
```