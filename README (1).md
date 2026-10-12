# COVID-19 Chest X-Ray Image Classification

A deep-learning project that classifies chest X-ray images into three
categories: **COVID**, **Normal**, and **Viral Pneumonia**. The model
was developed with TensorFlow/Keras in an Amazon SageMaker notebook,
with Amazon S3 used for dataset storage. A Flask-based web interface was
also prepared for image upload and prediction.

> **Important medical disclaimer:** This project is an
> educational/research prototype only. It is not validated for clinical
> use and must not be used to diagnose, treat, or rule out any medical
> condition.

## Project Overview

The goal is to explore how convolutional neural networks (CNNs) can
learn visual patterns from chest X-ray images and classify them into one
of three dataset labels.

### Classes

-   `Covid`
-   `Normal`
-   `Viral Pneumonia`

### Tools and Technologies

-   **Python**
-   **TensorFlow / Keras** --- model development and training
-   **CNN** --- image classification
-   **Amazon SageMaker** --- notebook-based development
-   **Amazon S3** --- dataset storage
-   **Flask** --- web application backend
-   **HTML/CSS** --- upload interface
-   **NumPy** --- array and prediction handling

## Model Details

The model is a sequential CNN with the following main components:

1.  Input images resized to **128 × 128 pixels**
2.  Data augmentation using random horizontal flips, rotations, and zoom
3.  Pixel rescaling inside the model
4.  Three convolutional layers with max-pooling
5.  Global average pooling
6.  Dense layer and dropout
7.  Softmax output layer for the three classes

**Training configuration recorded in the notebook:**

-   Image size: `128 × 128`
-   Batch size: `8`
-   Optimizer: Adam
-   Loss function: categorical cross-entropy
-   Maximum planned epochs: `15`
-   Early stopping based on validation loss

## Results

The recorded test accuracy was **66.67% on a test set of 66 images**.

This is a baseline result on a small dataset, not evidence of clinical
reliability. Performance may vary with image quality, data distribution,
and images from sources not represented in the training data. The
notebook also includes code to calculate a confusion matrix and
per-class precision, recall, and F1-score.

## Repository Structure

Arrange the project files in this structure:

``` text
covid19-image-classification/
├── COVID19_Image_Classification.ipynb
├── covid19_model.keras
├── app.py
├── templates/
│   └── index.html
├── covid19_dataset/              # local dataset; usually not committed
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
```

The dataset is expected to be arranged in class-specific folders. The
dataset itself is not included in this README; add it only if you have
permission to redistribute it and it complies with its license and
privacy requirements.

## Setup

### 1. Clone the repository

``` bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

Replace the URL and repository name with your own GitHub details.

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file with compatible versions for the
environment where you tested the project. The main packages used by the
project are:

``` text
tensorflow
numpy
Flask
Pillow
```

Then install them:

``` bash
pip install -r requirements.txt
```

TensorFlow installation requirements depend on your Python version and
operating system. Use a compatible environment and verify that
TensorFlow imports successfully before running the app.

### 4. Add the model and dataset

Place `covid19_model.keras` in the project root. For training or
evaluation, arrange the dataset under `covid19_dataset/train/` and
`covid19_dataset/test/`, with one subfolder per class.

The notebook originally downloads the `train/` and `test/` prefixes from
an Amazon S3 bucket. If you use your own bucket, update the bucket name
and paths in the notebook. Do not commit AWS credentials or access keys
to GitHub.

## Run the Notebook

Open `COVID19_Image_Classification.ipynb` in Jupyter or Amazon SageMaker
and run the cells in order. The notebook covers dataset loading,
preprocessing, augmentation, model training, evaluation,
confusion-matrix calculation, saving/loading the model, and a sample
prediction.

## Run the Flask Web App

If `app.py` and `templates/index.html` are present and the dependencies
are installed in the **same Python environment**, start the application
with:

``` bash
python app.py
```

Open the local address printed by Flask in your browser. If running on a
remote SageMaker instance, additional port forwarding or a supported
notebook proxy may be required; binding Flask to `0.0.0.0` alone does
not make the application publicly accessible.

The interface is intended to accept `.jpg`, `.jpeg`, and `.png` images
and display a predicted class with a confidence score.

**Preprocessing note:** the saved model includes a `Rescaling(1./255)`
layer. During inference, pass image pixel values in their usual 0--255
range and do **not** divide by 255 a second time before calling the
model.

## Limitations

-   The dataset and test set are small, so results may not generalize to
    other hospitals, scanners, or patient populations.
-   The model may make incorrect predictions and its confidence score is
    not a measure of clinical certainty.
-   The labels reflect the dataset classes; a model prediction does not
    confirm a medical diagnosis.
-   The web app's environment and deployment should be tested before
    presenting it as a working live demo.
-   This project is for learning and demonstration, not clinical
    decision-making.

## Future Improvements

-   Increase dataset size and evaluate data quality and class balance.
-   Use stratified evaluation and report class-wise metrics.
-   Compare the baseline CNN with transfer-learning models.
-   Add model versioning and reproducible training configuration.
-   Test the application end-to-end in one verified Python environment.
-   Consider responsible deployment, privacy, and appropriate clinical
    validation before any real-world use.

## Author

**Your Name**\
MBA in Artificial Intelligence & Data Science\
Add your LinkedIn profile and GitHub profile here.

## License

Add a license only after confirming that you have the rights to license
the code and that the dataset's terms permit your intended use. Dataset
licensing and code licensing may be different.
