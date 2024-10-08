# My CV helper tools

A collection of my personal helper tools and scripts for working with images, files and folders in CV tasks.

## Work with folders, files or create datasets

### `dataset_split.ipynb`

Split folders with files (e.g. images) into train, validation and test (dataset) folders.

see: [split-folders](https://github.com/jfilter/split-folders)

default: train 80%, val 10%, test 10%

## `merge_subfolder_images.ipynb`

Merge all images from a folder and its subfolders into a single folder. Recombine split images in subfolder structures

### `duplicate_images.ipynb`

Duplicate an image by the specified factor.

### `delete_random_images.py`

Delete random images from a folder. Specify a number of images to be left.

### Ms PowerToys PowerRename

Rename all files. see: https://learn.microsoft.com/de-de/windows/powertoys/powerrename

Note: Activate RegEx

```
(.*).jpeg

name_${padding=4;increment=1;start=1}

```

### TeraCopy

Copy your files faster and more securely

For Windows: https://www.codesector.com/teracopy

## Manipulate images

### `resize_images.ipynb`

Resize images to a new target resolution. Works with a folder with subfolders.

### `grayscale_blur_noise_image_creator.ipynb`

Apply blur and grayscale noise to a given input image.

### `auto_greyscale_blur_noise_image_creator.ipynb`

Create a new dataset with X random versions with blur and grayscale noise of each image. Rename the images and duplicate the annotation label files. This method makes it possible to generate a larger dataset from fewer images by generating variations of the original images and also eliminates the need to generate new annotations by copying the old ones. This is a data augmentation method.

## Docs and Plotting

### `doc_image_shower.ipynb`

Create a plot to show the first X number of images from a folder in a grid plot.

## Annotation Tool

- [Computer Vision Annotation Tool (CVAT)](https://github.com/cvat-ai/cvat): Online or self-hosted with Docker


## Requirements

```
split-folders
ipykernel
matplotlib
numpy
```

## My TODO:

- Refactor
