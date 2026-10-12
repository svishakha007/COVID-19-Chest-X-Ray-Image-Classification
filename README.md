COVID-19 Chest X-Ray Image Classification
A deep-learning project that classifies chest X-ray images into three categories: COVID, Normal, and Viral Pneumonia. The model was developed with TensorFlow/Keras in an Amazon SageMaker notebook, with Amazon S3 used for dataset storage. A Flask-based web interface was also prepared for image upload and prediction.

Important medical disclaimer: This project is an educational/research prototype only. It is not validated for clinical use and must not be used to diagnose, treat, or rule out any medical condition.

Project Overview
The goal is to explore how convolutional neural networks (CNNs) can learn visual patterns from chest X-ray images and classify them into one of three dataset labels.

Classes:

Covid
Normal
Viral Pneumonia

Tools and Technologies:

Python
TensorFlow / Keras --- model development and training
CNN --- image classification
Amazon SageMaker --- notebook-based development
Amazon S3 --- dataset storage
Flask --- web application backend
HTML/CSS --- upload interface
NumPy --- array and prediction handling

Model Details
The model is a sequential CNN with the following main components:

Input images resized to 128 × 128 pixels
Data augmentation using random horizontal flips, rotations, and zoom
Pixel rescaling inside the model
Three convolutional layers with max-pooling
Global average pooling
Dense layer and dropout
Softmax output layer for the three classes
Training configuration recorded in the notebook:

Image size: 128 × 128
Batch size: 8
Optimizer: Adam
Loss function: categorical cross-entropy
Maximum planned epochs: 15
Early stopping based on validation loss

Results
The recorded test accuracy was 66.67% on a test set of 66 images.

This is a baseline result on a small dataset, not evidence of clinical reliability. Performance may vary with image quality, data distribution, and images from sources not represented in the training data. The notebook also includes code to calculate a confusion matrix and per-class precision, recall, and F1-score.

Repository Structure:

covid19-image-classification/
├── COVID19_Image_Classification.ipynb
├── covid19_model.keras
├── app.py
├── templates/
│   └── index.html
├── covid19_dataset/
│   ├── train/
│   │   ├── Covid/
│   │   ├── Normal/
│   │   └── Viral Pneumonia/
│   └── test/
│       ├── Covid/
│       ├── Normal/
│       └── Viral Pneumonia/
├── requirements.txt
└── README.md
