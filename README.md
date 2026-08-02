# MNIST Digit Recognition using CNN

# Live Demo
🔗https://handwrittendigitpredictor-lgbuqxku9pby2ybccqjbuf.streamlit.app/

## 📌 Project Overview

This project implements a **Convolutional Neural Network (CNN)** using **TensorFlow/Keras** to recognize handwritten digits from the **MNIST** dataset. The model is trained to classify grayscale images of digits (0–9) with high accuracy.

---

## 🚀 Features

* Handwritten digit recognition (0–9)
* Built using TensorFlow and Keras
* Image preprocessing and normalization
* CNN-based deep learning model
* Model training and evaluation
* Visualization of training accuracy and loss
* Prediction on test images

---

## 📂 Dataset

The project uses the **MNIST** dataset, which is included with TensorFlow/Keras.

Dataset Details:

* **70,000** grayscale images
* **60,000** training images
* **10,000** testing images
* Image size: **28 × 28 pixels**
* **10 output classes (digits 0–9)**

---

## 🛠️ Technologies Used

* Python
* TensorFlow
* Keras
* NumPy
* Matplotlib

---

## 🧠 Model Architecture

The CNN model consists of the following layers:

1. Convolutional Layer (ReLU)
2. Max Pooling Layer
3. Convolutional Layer (ReLU)
4. Max Pooling Layer
5. Flatten Layer
6. Dense Layer (ReLU)
7. Output Layer (Softmax)

---

## 📊 Model Performance

| Metric            | Value   |
| ----------------- | ------- |
| Training Accuracy | ~99%    |
| Test Accuracy     | ~98–99% |

*Note: Results may vary slightly depending on training parameters.*

---

## 📁 Project Structure

```
MNIST-Digit-Recognition/
│
├── MNIST_Digit_Recognition.ipynb
├── README.md
├── requirements.txt
├── .gitignore
└── images/
    └── sample_prediction.png


## 📈 Results

The trained CNN model successfully recognizes handwritten digits with high accuracy and demonstrates the effectiveness of deep learning for image classification tasks.

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Data augmentation
* Deploy the model using Streamlit or Flask
* Convert the model to TensorFlow Lite for mobile deployment
* Experiment with deeper CNN architectures

---

## 👨‍💻 Author

**Abhishek Sharma**

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it for learning and educational purposes.
