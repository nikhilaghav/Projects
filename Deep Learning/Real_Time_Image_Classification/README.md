📌 Description

This project is a real-time image classification system that uses a webcam to capture live video frames and classify the objects present in the frame.

The project uses the MobileNetV2 Convolutional Neural Network (CNN), which is a pre-trained model trained on the ImageNet dataset.

The webcam continuously captures images, preprocesses them according to the MobileNetV2 requirements, and predicts the most likely object along with its confidence score.

🚀 Features
  
  Real-time webcam image classification
  
  Uses a pre-trained MobileNetV2 CNN
  
  Trained on the ImageNet dataset
  
  Converts webcam frames from BGR to RGB
  
  Resizes images to 224 × 224
  
  Performs ImageNet-specific preprocessing
  
  Displays the predicted class and confidence percentage
  
  Press q to exit the application

🧠 Technologies Used

  Python
    
  OpenCV

  NumPy

  TensorFlow / Keras

  MobileNetV2
  
  ImageNet


#######################################################

project flow

#######################################################


1-Load MobileNetV2

  Pretrained on ImageNet dataset

2-Open Webcam

  Capture live video frames using OpenCV

3-Image Preprocessing

  BGR → RGB → Resize → Normalize

4-MobileNetV2 Prediction

  Predict the object category

5-Decode Prediction

  Convert prediction into a readable label

6-Display Result

  Show object name and confidence on webcam  
 
