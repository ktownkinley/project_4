# CNN for Respiratory Infection Detection - Final Project 

# Overview
This repository and project revolves around a CNN model that differentiates between benign xrays and pneumonia ridden xrays. We used a dataset provided by Paul Mooney posted on Kaggle that contains deidentified xray images separated by "normal" and "pneumonia" and then split into testing, training, and validation folders to produce a model with an 87% precision and 87% loss. This repository houses everything required to recreate the model, the code to host it onto a website, and the data itself.
# Index
* The "flask_project" folder houses the backend flask and database files
* The "CNN Model" folder houses the primary model, a model designed for a guessing game housed on the website, and the jupyter notebook files used to create them
* The main repository folder has the model exported as .h5, along with the .readme, .gitignore, etc.
# Explore Results
As stated, this model has a precision of 87% and a loss of 87%, making it quite viable at it's task. Previous iterations of the model had some bias, and tweaking the parameters for it was required. This could also be due to the smaller sample size we used to train it to conserve time, but in the end it got smoothed out by using the larger sample size, and overall has improved.
# Technical Summary
Tensorflow was the backbone for the model, as this is what we used to build and train the model. Flask was used for the backend. Besides carousel, base javascript,html, and css was used to build the site to be hosted onto flask. 
# Usage 
This model can be used for any front facing chest xray to determine if said xray is of a healthy person or one with pneumonia simply by downloading the chest_Xray.h5 file and importing it into your code with tensorflow. No credit to this repo is necessary(see the MIT license), however please credit the dataset to Paul Mooney.