📌 Project Overview

This project uses Unsupervised Machine Learning to group mall customers into different customer segments based on their:

Annual Income

Spending Score

The project uses the K-Means Clustering algorithm to identify groups of customers with similar characteristics.

Since this is an unsupervised learning problem, there is no predefined target variable. The algorithm itself discovers the groups (clusters) present in the data.

🎯 Objective

The main objective of this project is to divide mall customers into different groups based on their annual income and spending behavior.

The project demonstrates the following Machine Learning workflow:

Dataset
   ↓
Load Data
   ↓
Check Missing Values
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Elbow Method
   ↓
Select Optimal K
   ↓
Build K-Means Model
   ↓
Assign Clusters
   ↓
Display Results

📊 Dataset

The project uses:

Mall_Customers.csv

The dataset contains information about mall customers.

The project specifically uses two features:

  AnnualIncome

  SpendingScore

Selected Features                 Feature	Description

AnnualIncome	                    Annual income of the customer

SpendingScore	                   Spending behavior/score of the customer

These two features are used to determine customer groups.
