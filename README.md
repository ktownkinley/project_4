# CNN for Respiratory Infection Detection - Final Project 

# Overview
This repository and project revolves around a Covolutionnal Nerual Network (CNN) model that predicts whether pneumonia is present in an anterior chest xray. We used a dataset provided by Paul Mooney posted on Kaggle that contains deidentified xray images separated by "normal" and "pneumonia" and then split into training and testing  folders. This repository houses everything required to recreate the model, the code to host it onto a website, and the data itself.

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
    * Model performance on predicting pneumonia.
        * Precision 87.1%:
           *  Out of the images predicted by the model as having pneumonia, roughly 13% were normal.
        * Recall 87.5%:
           * This means that 12.6% of xrays with pneumonia were not predicted by the model.
    * Model performance on normal xrays.
        *  Precision 87.4%:
           *  Meaning of the loans that were predicted as high-risk, 15% were actually healthy,
        *  Recall 91%:
           *  Out of all of the high-risk loans, 9% weren't predicted correctly by the model.
     *  Overall accuracy 99%:
        *  Out of all of the predictions, only 1% wasn't correct. However, this metric is slightly skewed as there was more healthy loans, which the model       performed better on than high risk loans.

# Exploring Results
After the model was trained, it was tested on xray images it has never seen before to get a has a precision of 87% and a loss of 87%, making it quite viable at it's task. Previous iterations of the model had some bias, and tweaking the parameters for it was required. This could also be due to the smaller sample size we used to train it due to limited RAM capabilites in the free version of Google Colab.

# Technical Summary
Tensorflow was the backbone for the model, as this is what we used to build and train the model. Flask was used for the backend. Besides carousel, base javascript,html, and css was used to build the site to be hosted onto flask. 
# Usage 
This model can be used for any front facing chest xray to determine if said xray is of a healthy person or one with pneumonia simply by downloading the chest_Xray.h5 file and importing it into your code with tensorflow. No credit to this repo is necessary(see the MIT license), however please credit the dataset to Paul Mooney.
