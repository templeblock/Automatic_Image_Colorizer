# Automatic Image Colorizer

<p align="center">
  <img src="static/img/demo_pics/demo_pic1.png"/>
</p>

Automatically colors black & white images 

Components:

- Deep Learning - Computer Vision
- Web development using Python (Flask)
- Algorithm modification for website integration
- Deployment on AWS cloud (Elastic Beanstalk)

Based off of a pre-trained image colorization [algorithm](https://arxiv.org/abs/1603.08511) made by Richard Zhang, Phillip Isola, and Alexei A. Efros.

### Instructions

- Go to the website: [Automatic Image Colorizer](http://automaticimagecolorizer1028.us-east-1.elasticbeanstalk.com)
- Upload a black and white image (hint: landscapes and portraits work the best)
- Press 'Submit' and wait for the algorithm to finish and display the fully colored image (bigger images take longer)

### Demo

<p align="center">
  <img src="static/img/auto_colorizer_demo1.gif"/>
</p>



#### Citation

```
@inproceedings{zhang2016colorful,
  title={Colorful Image Colorization},
  author={Zhang, Richard and Isola, Phillip and Efros, Alexei A},
  booktitle={ECCV},
  year={2016}
}

@article{zhang2017real,
  title={Real-Time User-Guided Image Colorization with Learned Deep Priors},
  author={Zhang, Richard and Zhu, Jun-Yan and Isola, Phillip and Geng, Xinyang and Lin, Angela S and Yu, Tianhe and Efros, Alexei A},
  journal={ACM Transactions on Graphics (TOG)},
  volume={9},
  number={4},
  year={2017},
  publisher={ACM}
}
```