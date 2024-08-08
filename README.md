# CNN for Respiratory Infection Detection - Final Project 

# Overview
This repository and project focus on a Convolutional Neural Network (CNN) model designed to predict the presence of pneumonia in anterior chest X-ray images. The dataset, provided by Paul Mooney and posted on Kaggle, contains de-identified X-ray images categorized as "normal" or "pneumonia" and is split into training and testing folders. This repository includes everything needed to recreate the model, the code to deploy it on a website, and the dataset itself.

Data Source:
https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia/data

- Our database engineering was handled through MongoDB, Flask, and python
- API calls and analysis were articulated in Javascript files
- Front-end rendering was built with HTML and CSS
- We used a new-to-us python library flask_pymongo that allowed our Flask application to connect to a MongoDB Atlas instance

# Index
* The "flask_project" folder houses the backend flask and database files as well as the static files for front end development.
* The model itself was exported as .h5 file found in the "model-xray/Model" folder
* The "CNN Model" folder houses the jupyter notebook file that trained and tested the model. Also, the outputted graphs and charts from the model's performance in pneumonia detection.

# Results

* CNN Model:
    * Model performance on pneumonia xrays.
        * Precision 87.4%:
           *  Out of all images predicted by the model as having pneumonia, 13% were normal.
        * Recall 87%:
           * This means that 12.6% of xrays with pneumonia were not predicted by the model.
    * Model performance on normal xrays.
        *  Precision 87.4%:
           *  Meaning of the xrays that were predicted as normal, roughly 13% had pneumonia.
        *  Recall 87%:
           *  Out of all of the nomral xrays, 13% weren't predicted correctly by the model.
     *  Overall accuracy 87.3%:

# Exploring Results
After training the model, it was tested on unseen X-ray images, achieving a precision of 87% and a loss of 87%. While this indicates that the model is fairly accurate, the margin of error may still be too high for practical use in predicting health outcomes. Earlier versions of the model struggled with overfitting, performing well on training data but poorly on testing images. To address this, techniques such as Dropout, Regularization, and Early Stopping were applied to mitigate overfitting. However, further experimentation is needed to optimize the model's accuracy. The model's performance may be limited by the smaller sample size used for training, a constraint caused by limited RAM capabilities in the free version of Google Colab. Training the model on a larger dataset could potentially improve its accuracy.

# Technical Summary
Tensorflow was the backbone for the model, as this is what we used to build and train the model. Flask was used for the backend. While javascript,html, and css was used to build the site to be hosted onto flask. 

# Usage 
This model can be used for any front facing chest xray to determine if said xray is of a healthy person or one with pneumonia simply by downloading the chest_Xray.h5 file and importing it into your code with tensorflow. No credit to this repo is necessary(see the MIT license), however please credit the dataset to Paul Mooney.
