# Breast Cancer Random Forest Classification with Docker Deployment

This project is a breast cancer classification system based on the Wisconsin Breast Cancer dataset. We've trained a Random Forest model using scikit-learn to classify breast cancer tumors as benign or malignant. Additionally, we've containerized the model deployment using Docker.

## Table of Contents

- [Dataset](#dataset)
- [Model Training](#model-training)
- [Docker Deployment](#docker-deployment)
- [Usage](#usage)


## Dataset

We used the Wisconsin Breast Cancer dataset, which is a widely used dataset for breast cancer classification. This dataset contains features derived from a digitized image of a fine needle aspirate (FNA) of a breast mass. The features describe various characteristics of cell nuclei present in the image.

## Model Training

In this project, we utilized the scikit-learn library to train a Random Forest classification model. Random Forest is an ensemble learning method that combines multiple decision trees to make predictions. Our model has been trained on this dataset to classify breast tumors as benign or malignant with a high degree of accuracy.

## Docker Deployment

To make the model accessible and deployable, we've encapsulated it in a Docker container. Docker provides a consistent and isolated environment for deploying the model, making it easy to share and run across different systems. This Docker container can be deployed on various platforms that support Docker, such as cloud providers or on-premises servers.

## Usage

To use this project, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Build the Docker container: `docker build -t breast-cancer-classifier .`
3. Run the Docker container: `docker run -p 8080:8080 breast-cancer-classifier`
4. Access the model API at `http://localhost:8080` or the appropriate address if deployed elsewhere.

You can now send POST requests to the model API with data for breast cancer classification.

Example using Python requests in the testapp file provided
