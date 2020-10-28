# Notes

## Intro

Project

* Website with a deep neural network image colorization algorithm behind it.  Allows users to use the image colorization algo online
* Disclaimer: I didn't create the algorithm. I got a pre-trained algorithm from a Phd at UC Berkeley. 

Inspiration: 

* I learned when I was teaching a section on deep learning at GWU fin-tech bootcamp,  that restoring black & white images nowadays is done by ML. This blew my mind away, realizing that the colored (or 'restored') films and documentaries are actually restored by machines. 
* I wanted to try and create my own colorization algorithm but realized how difficult it is. The good algorithms are trained on over 1M images and the best algorithm right now only passes the colorization turing test 32% of the trials. This is a work that Phd's from all over the world are currently still working on. I knew this was going to take me ages.
* Instead, I decided to use a pre-trained algorithm developed by a Phd from Berkeley to build a program that allows people to try this out, bc surprisingly, altough many of these algorithms are open source and available online,  they are not available for non-technical people. 

Goal: 

* Learn the non-ML components of data science project (i.e. everything but the ML algorithm). This includes the website for UI, modifying and connecting the algorithm to UI, and deploying it online using AWS. 

#### Technologies

* Deep Learning Algorithm
* Python: Flask, matplotlib, torch, scikit-image
* Front-end Technologies: HTML, CSS, Bootstrap
* AWS - Elastic Beanstalk
* reCAPTCHA

## Procedures

1. Explore and find the best performing algorithm (pre-trained model)
2. Build a flask website with upload and display image function
3. Modify the algorithm to fit with the website (allow file input from website, path for pre-trained algorithms, output results to website, removing/modifying code that interferes with website and deployment)
4. Modify flask app to display image output from the algorithm
5. Deploy on AWS Elastic Beanstalk

#### Biggest Challenge

* Cache problem - I wanted to upload all pictures in the same name to eliminate the need for storage management. However, the problem was that even if new files are uploaded, the website will display the previously uploaded file that is in the cache instead of the new image that is in the storage. My solution was to disable the cache, which, in my use case, was enough to solve the problem. 
* AWS - MemoryError - EC2 instance deployment kept failing during application dependencies installation. Using a bigger EC2 instance solved it.
* AWS - Backend crashing - I didn't realize it was this problem at first. "upstream prematurely closed connection" error. Not very clear as to what exactly happened. Many possibilities including NGINX config issue, memory, and timing out. I tried all of the suggested answers online but none of them worked (bigger EC2, NGINX config to increase memory and timeout). I solved it completely by accident while fixing another issue with argparse not allowing 'flask run' command. It turned out that the way AWS was starting my flask program was passing in arguments considered invalid by argparse in the colorization algorithm. Solved it by removing argparse code. 

#### Reflection - What I learned 

* A lot of information in the EC2 logs. Can even view who are visiting the website and what they are doing (POST requests)
* Debugging AWS is difficult. Documentation wasn't too helpful for debugging and the logs from EC2 isntances are either not very clear or helpful. 
* Fixing and modifying another program - I feel confident that I can begin contributing to open source projects.
* There are bots that roam all around the web looking for vulnerable websites. Learned of this after seeing unusual requests from suspicious IP addresses. Implemented reCAPTCHA on the website just in case since this website has a *naked* (not hidden behind a login) form. 