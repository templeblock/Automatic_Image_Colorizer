# Notes



## Intro

* What it is
* Inspiration

Automatic image colorization allows users to simply upload a grayscale (i.e. black and white) image and see it colorized. 

Learned that it was possible while teaching a section on Deep Learning. I've recently watched a documentary with colorized film from WWII and my realization that a machine have done the colorizaiton was fascinating. I first started playing around with it and decided to make a website and make it available for my friends to use it and try it out for themselves. 

## Description of Program

1. Explore and find the best performing algorithm (pre-treained model). A few models, including Caffe1 and Caffe2 deep learning framework model and 





Automatic colorization using deep neural networks.

## Reflection



#### Biggest Challenge

* Cache problem - I wanted to upload all pictures in the same name to eliminate the need for storage management. However, the problem was that even if new files are uploaded, the website will display the previously uploaded file that is in the cache instead of the new image that is in the storage. My solution was to disable the cache, which, in my use case, was enough to solve the problem. 

#### What I would have done better



#### Technologies Used

* Python
  * Packages: Flask, torch, scikit-image, matplotlib, argparse, Pillow

