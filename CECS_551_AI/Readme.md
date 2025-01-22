# CECS 551 - Artificial Intelligence Projects

This repository contains projects from the CECS 551 course on Artificial Intelligence, showcasing various implementations and experiments in machine learning and neural networks.

---

## Table of Contents

1. [Multi-Layer Perceptron (MLP)](#multi-layer-perceptron-mlp)
2. [Hyperparameter Tuning](#hyperparameter-tuning)
3. [Classification with CNN](#classification-with-cnn)
4. [Research Paper Review](#research-paper-review)

---

## Multi-Layer Perceptron (MLP)

**Description**:  
Implemented a multi-layer neural network without using external deep learning libraries like PyTorch or Keras. The goal was to approximate the XOR function using a feed-forward network. Key steps included:
- Derivation and implementation of backpropagation formulas.
- Optimization using gradient descent.
- Visualization of loss over epochs and prediction outputs.

**Key Features**:
- Manual backpropagation implementation.
- Gradient descent optimization.
- Plotting loss vs. epochs.

**Repository**:  
[Multi-Layer Perceptron]([https://github.com/ishank-dev/CECS551-Assignment2](https://github.com/ishank-dev/CECS_CSULB_2026/blob/main/CECS_551_AI/Assignment_2/Assignment%202%20MLP%20(4).ipynb)

---

## Hyperparameter Tuning

**Description**:  
Performed hyperparameter tuning for a neural network using various optimizers, including:
- Stochastic Gradient Descent with Momentum (SGD)
- AdaGrad
- RMSProp
- Adam

The MNIST dataset was used to train and validate the models, testing various combinations of learning rates, batch sizes, and other parameters to find the best-performing configurations.

**Key Features**:
- Explored multiple optimizers.
- Plotted training and validation loss curves.
- Identified optimal hyperparameters for best test accuracy.

**Repository**:  
[Hyperparameter Tuning]([https://github.com/ishank-dev/CECS551-Assignment3](https://github.com/ishank-dev/CECS_CSULB_2026/blob/main/CECS_551_AI/Assignment_3/Assignment%20AI%20(3)%20(5).ipynb))

---

## Classification with CNN

**Description**:  
Designed and experimented with Convolutional Neural Networks (CNNs) to classify images in the CIFAR-100 dataset. The focus was on:
- Experimenting with activation functions, optimizers, and architectures.
- Dividing the dataset for training, validation, and testing.
- Benchmarking against other models on the CIFAR-100 leaderboard.

**Key Features**:
- Experimentation with model architectures.
- Benchmarking against the CIFAR-100 leaderboard.
- Comprehensive reporting of results.

**Repository**:  
[Classification with CNN](https://github.com/ishank-dev/CECS_CSULB_2026/blob/main/CECS_551_AI/Assignment_4/Assignment%204%20Final%20AI%20(2)%20(1).ipynb)

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/ishank-dev/CECS551-Assignments.git
