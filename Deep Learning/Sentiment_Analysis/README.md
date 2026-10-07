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
