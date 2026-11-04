🎬 Movie Review Sentiment Analysis using LSTM

A Deep Learning project that performs sentiment analysis on movie reviews using an LSTM (Long Short-Term Memory) neural network.

The model is trained on the IMDB Movie Review Dataset and classifies a movie review as either Positive or Negative.

📌 Project Overview

Sentiment Analysis is a Natural Language Processing (NLP) task used to determine the emotional tone of a text.

In this project, a movie review is given as input and the LSTM model predicts whether the review expresses:

 0 → Negative Sentiment

 1 → Positive Sentiment

Example

Input:
 "This movie was excellent and I really enjoyed it."

Output:

 Positive

🧠 Technologies Used
Python

TensorFlow

Keras

Natural Language Processing (NLP)

Deep Learning

LSTM

IMDB Dataset

📊 Dataset

The project uses the IMDB Movie Review Dataset provided by TensorFlow/Keras.

The dataset contains:

25,000 training reviews

25,000 testing reviews

Binary sentiment labels

The model considers the 10,000 most frequent words from the dataset.

VOCAB_SIZE = 10000

################################################################
 Complete project flow
#################################################################

1. Load IMDB Dataset

    25,000 training reviews + 25,000 testing reviews


2. Decode Reviews

    Convert encoded numbers into readable words for understanding


3. Preprocessing

    Limit vocabulary to 10,000 words and pad/truncate reviews to 200 words


4. Build LSTM Model
    Embedding Layer
    
    10000 words → 32-dimensional vectors
    
    LSTM Layer
    
    64 units – learns sequence patterns
    
    Dense Layer
    
    Sigmoid activation – predicts probability

5. Compile Model

    Adam optimizer, Binary Crossentropy loss, Accuracy metric


6. Train Model

   3 epochs, batch size 64, validation split 20%


7. Evaluate Model

   Test using X_test and Y_test


8. Make Prediction

    Predict whether a review is Positive or Negative
