import pandas as pd
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


BASE_DIR = Path(__file__).resolve().parent

Border = "-" * 40


########################################
# Step 1 : Load the dataset
########################################

def LoadData(DataPath):

    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Dataset loaded successfully")

    print("Initial entries from dataset are : ")
    print(df.head())

    return df


########################################
# Step 2 : Data Analysis (EDA)
########################################

def DataAnalysis(df):

    print(Border)
    print("Step 2 : Data Analysis (EDA)")
    print(Border)

    print("Shape of dataset : ", df.shape)

    print("Column names : ", list(df.columns))

    print("Missing values per column : ")
    print(df.isnull().sum())

    print("Class distribution : ")
    print(df["Class"].value_counts())

    print("Statistical report of dataset : ")
    print(df.describe())


########################################
# Step 3 : Clean the dataset
########################################

def CleanData(df):

    print(Border)
    print("Step 3 : Clean the dataset")
    print(Border)

    df = df.dropna().copy()

    print("Dataset cleaned successfully")

    print("Shape after cleaning : ", df.shape)

    return df


########################################
# Step 4 : Separate Features and Labels
########################################

def SeparateFeatures(df):

    print(Border)
    print("Step 4 : Decide Independent & Dependent variables")
    print(Border)

    X = df.drop(columns=["Class"])

    Y = df["Class"]

    print("X Shape : ", X.shape)
    print("Y Shape : ", Y.shape)

    print("Input columns : ", X.columns.tolist())
    print("Output column : Class")

    return X, Y


########################################
# Step 5 : Split the dataset
########################################

def SplitData(X, Y):

    print(Border)
    print("Step 5 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Dataset splitting activity done")

    print("X_train : ", X_train.shape)
    print("X_test : ", X_test.shape)

    print("Y_train : ", Y_train.shape)
    print("Y_test : ", Y_test.shape)

    return X_train, X_test, Y_train, Y_test


########################################
# Step 6 : Feature Scaling
########################################

def ScaleFeatures(X_train, X_test):

    print(Border)
    print("Step 6 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling done successfully")

    return X_train_scaled, X_test_scaled, scaler


########################################
# Step 7 : Hyperparameter Tuning
########################################

def HyperparameterTuning(X_train, Y_train):

    print(Border)
    print("Step 7 : Hyperparameter Tuning")
    print(Border)

    accuracy_scores = []

    K_values = range(1, 21)

    for k in K_values:

        # Scaling is performed inside each CV fold
        pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("knn", KNeighborsClassifier(n_neighbors=k))
        ])

        scores = cross_val_score(
            pipeline,
            X_train,
            Y_train,
            cv=5,
            scoring="accuracy"
        )

        accuracy = scores.mean()

        accuracy_scores.append(accuracy)

    print("Cross-validation accuracy report : ")

    for k, accuracy in zip(K_values, accuracy_scores):

        print(
            "K =", k,
            "Mean CV Accuracy =", accuracy
        )

    return K_values, accuracy_scores


########################################
# Step 8 : Find the best value of K
########################################

def FindBestK(K_values, accuracy_scores):

    print(Border)
    print("Step 8 : Find the best value of K")
    print(Border)

    BestIndex = accuracy_scores.index(max(accuracy_scores))

    BestK = list(K_values)[BestIndex]

    BestAccuracy = accuracy_scores[BestIndex]

    print("Best value of K : ", BestK)

    print("Best cross-validation accuracy : ", BestAccuracy * 100)

    return BestK


########################################
# Step 9 : Build the final model
########################################

def CreateModel(BestK):

    print(Border)
    print("Step 9 : Build the final model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=BestK)

    print("KNN model created successfully")

    return model


########################################
# Step 10 : Train the final model
########################################

def TrainModel(model, X_train_scaled, Y_train):

    print(Border)
    print("Step 10 : Train the final model")
    print(Border)

    model.fit(X_train_scaled, Y_train)

    print("Model trained successfully")

    return model


########################################
# Step 11 : Test the final model
########################################

def TestModel(model, X_test_scaled, Y_test):

    print(Border)
    print("Step 11 : Test the final model")
    print(Border)

    Y_pred = model.predict(X_test_scaled)

    print("Model testing done")

    print("Expected answers : ")
    print(Y_test.values)

    print("Predicted answers : ")
    print(Y_pred)

    return Y_pred


########################################
# Step 12 : Evaluate model performance
########################################

def EvaluateModel(Y_test, Y_pred):

    print(Border)
    print("Step 12 : Evaluate the model performance")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ", accuracy * 100)

    print("Confusion Matrix : ")

    cm = confusion_matrix(Y_test, Y_pred)

    print(cm)

    print("Classification Report : ")

    print(classification_report(Y_test, Y_pred))


########################################
# Step 13 : Visualisation of K values
########################################

def VisualizeKValues(K_values, accuracy_scores):

    print(Border)
    print("Step 13 : Visualisation of K values")
    print(Border)

    plt.figure(figsize=(8, 5))

    plt.plot(
        K_values,
        accuracy_scores,
        marker="o"
    )

    plt.title("K Values vs Cross-Validation Accuracy")

    plt.xlabel("Value of K")

    plt.ylabel("Mean Cross-Validation Accuracy")

    plt.grid(True)

    plt.xticks(list(K_values))

    plt.show()


########################################
# Step 14 : Save trained model
########################################

def SaveModel(model, scaler, feature_names):

    print(Border)
    print("Step 14 : Save trained model")
    print(Border)

    model_data = {
        "model": model,
        "scaler": scaler,
        "features": feature_names
    }

    joblib.dump(
        model_data,
        BASE_DIR / "WinePredictor.pkl"
    )

    print("Model saved successfully")


########################################
# Main Function
########################################

def main():

    # Step 1 : Load Dataset
    df = LoadData(BASE_DIR / "WinePredictor.csv")

    # Step 2 : Data Analysis
    DataAnalysis(df)

    # Step 3 : Clean Dataset
    df = CleanData(df)

    # Step 4 : Separate Features and Labels
    X, Y = SeparateFeatures(df)

    # Step 5 : Split Dataset
    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    # Step 6 : Feature Scaling
    X_train_scaled, X_test_scaled, scaler = ScaleFeatures(
        X_train,
        X_test
    )

    # Step 7 : Hyperparameter Tuning
    K_values, accuracy_scores = HyperparameterTuning(
        X_train,
        Y_train
    )

    # Step 8 : Find Best K
    BestK = FindBestK(K_values, accuracy_scores)

    # Step 9 : Create Model
    model = CreateModel(BestK)

    # Step 10 : Train Model
    model = TrainModel(
        model,
        X_train_scaled,
        Y_train
    )

    # Step 11 : Test Model
    Y_pred = TestModel(
        model,
        X_test_scaled,
        Y_test
    )

    # Step 12 : Evaluate Model
    EvaluateModel(Y_test, Y_pred)

    # Step 13 : Visualize K Values
    VisualizeKValues(K_values, accuracy_scores)

    # Step 14 : Save Model
    SaveModel(
        model,
        scaler,
        X.columns.tolist()
    )


########################################
# Starter of the program
########################################

if __name__ == "__main__":
    main()
