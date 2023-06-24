# Analysis of Scanned Prescription
This repository contains the code and resources for the project "Analysis of Scanned Prescription." The objective of this project is to recognize medicines prescribed by doctors from scanned prescriptions.

## Project Overview
In this project, we aim to improve the detection of text parts in scanned prescription images and predict the medicine written by the doctor using pre-saved medicine data. The following steps were undertaken to achieve this:

1. Cleaning Scanned Images: The scanned images were preprocessed to remove watermarks and other artifacts that could hinder the detection of text areas.

2. Text Extraction: Using image processing techniques, we extracted the areas of the prescription that contained text, focusing on the relevant portions.

3. Medicine Prediction: Convolutional Neural Network (CNN) models were utilized to predict the medicine written by the doctor. The models were trained using the list of pre-saved medicines as the training data.

4. Technologies Used: The project utilized the following technologies:
    - OpenCV: A computer vision library used for image preprocessing and text extraction.
    - TensorFlow: A popular deep learning framework used for training and deploying the CNN models.
