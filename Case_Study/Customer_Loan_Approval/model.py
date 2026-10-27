import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


BASE_DIR = Path(__file__).resolve().parent


# Step 1 : Load Data

#-----------------------------------------------------
#   Function Name : LoadData
#   Description :   Load the data from CSV
#   Input :         Name of CSV file
#   Output :        Data Frame
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def LoadData(filename):

    df = pd.read_csv(filename)

    print("Dataset loaded successfully")

    print("Shape of dataset : ", df.shape)

    print("First few records : ")
    print(df.head())

    return df


# Step 2 : Check Missing Values

#-----------------------------------------------------
#   Function Name : CheckMissingValues
#   Description :   Check missing values in dataset
#   Input :         Data Frame
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CheckMissingValues(df):

    print("Missing values : ")
    print(df.isnull().sum())

    print("Missing values checking completed")


# Step 3 : Separate Features and Labels

#-----------------------------------------------------
#   Function Name : SeparateFeatures
#   Description :   Separate features and target labels
#   Input :         Data Frame
#   Output :        Features and Labels
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SeparateFeatures(df):

    X = df.drop("LoanApproved", axis=1)

    Y = df["LoanApproved"]

    print("Feature and label separation completed")

    print("X shape : ", X.shape)

    print("Y shape : ", Y.shape)

    return X, Y


# Step 4 : Split Data

#-----------------------------------------------------
#   Function Name : SplitData
#   Description :   It performs dataset splitting
#   Input :         Features and Labels
#   Output :        4 subsets for training and testing
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SplitData(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Dataset splitting completed successfully")

    return X_train, X_test, Y_train, Y_test


# Step 5 : Scale Features

#-----------------------------------------------------
#   Function Name : ScaleFeatures
#   Description :   It performs feature scaling
#   Input :         Training and testing features
#   Output :        Scaled training and testing features
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def ScaleFeatures(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    print("Feature scaling completed successfully")

    return X_train_scaled, X_test_scaled, scaler


# Step 6 : Create Individual Models

#-----------------------------------------------------
#   Function Name : CreateModels
#   Description :   Create individual ML models
#   Input :         None
#   Output :        Logistic Regression, Decision Tree,
#                   and KNN models
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CreateModels():

    model_log = LogisticRegression(max_iter=1000)

    model_det = DecisionTreeClassifier(random_state=42)

    model_knn = KNeighborsClassifier(n_neighbors=5)

    print("Individual models created successfully")

    return model_log, model_det, model_knn


# Step 7 : Train Individual Models

#-----------------------------------------------------
#   Function Name : TrainIndividualModels
#   Description :   Train individual ML models
#   Input :         Models, training features and labels
#   Output :        Trained individual models
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def TrainIndividualModels(model_log, model_det, model_knn, X_train, Y_train):

    model_log.fit(X_train, Y_train)

    model_det.fit(X_train, Y_train)

    model_knn.fit(X_train, Y_train)

    print("Individual models trained successfully")

    return model_log, model_det, model_knn


# Step 8 : Evaluate Individual Models

#-----------------------------------------------------
#   Function Name : EvaluateIndividualModels
#   Description :   Test and evaluate individual models
#   Input :         Models, testing features and labels
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def EvaluateIndividualModels(model_log, model_det, model_knn, X_test, Y_test):

    Y_pred_log = model_log.predict(X_test)

    Y_pred_det = model_det.predict(X_test)

    Y_pred_knn = model_knn.predict(X_test)

    print("Accuracy of Logistic Regression model : ",
          accuracy_score(Y_test, Y_pred_log))

    print("Accuracy of Decision Tree model : ",
          accuracy_score(Y_test, Y_pred_det))

    print("Accuracy of KNN model : ",
          accuracy_score(Y_test, Y_pred_knn))


# Step 9 : Create Hard Voting Classifier

#-----------------------------------------------------
#   Function Name : CreateHardVotingModel
#   Description :   Create Hard Voting Classifier
#   Input :         Individual ML models
#   Output :        Hard Voting Classifier model
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CreateHardVotingModel(model_log, model_det, model_knn):

    model_voting = VotingClassifier(
        estimators=[
            ('logistic', model_log),
            ('decision_tree', model_det),
            ('knn', model_knn)
        ],
        voting='hard'
    )

    print("Hard Voting Classifier created successfully")

    return model_voting


# Step 10 : Create Soft Voting Classifier

#-----------------------------------------------------
#   Function Name : CreateSoftVotingModel
#   Description :   Create Soft Voting Classifier
#   Input :         Individual ML models
#   Output :        Soft Voting Classifier model
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CreateSoftVotingModel(model_log, model_det, model_knn):

    model_voting = VotingClassifier(
        estimators=[
            ('logistic', model_log),
            ('decision_tree', model_det),
            ('knn', model_knn)
        ],
        voting='soft'
    )

    print("Soft Voting Classifier created successfully")

    return model_voting


# Step 11 : Train Voting Model

#-----------------------------------------------------
#   Function Name : TrainVotingModel
#   Description :   It performs voting model training
#   Input :         Model, training features and labels
#   Output :        Trained voting model
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def TrainVotingModel(model, X_train, Y_train):

    model.fit(X_train, Y_train)

    print("Voting model trained successfully")

    return model


# Step 12 : Evaluate Voting Model

#-----------------------------------------------------
#   Function Name : EvaluateVotingModel
#   Description :   Test and evaluate voting classifier
#   Input :         Model, testing features and labels
#   Output :        Accuracy
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def EvaluateVotingModel(model, X_test, Y_test):

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is : ", accuracy)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test, Y_pred))

    return accuracy


# Step 13 : Save Model

#-----------------------------------------------------
#   Function Name : SaveModel
#   Description :   Save trained model and scaler
#   Input :         Model, scaler and feature names
#   Output :        PKL file
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SaveModel(model, scaler, feature_names):

    model_data = {
        "model": model,
        "scaler": scaler,
        "features": feature_names
    }

    joblib.dump(
        model_data,
        BASE_DIR / "LoanApprovalModel.pkl"
    )

    print("Model saved successfully")


#-----------------------------------------------------
#   Function Name : main
#   Description :   Entry point function
#   Input :         None
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def main():

    # Step 1 : Load Data
    df = LoadData(BASE_DIR / "Customer_Loan_Approval.csv")

    # Step 2 : Check Missing Values
    CheckMissingValues(df)

    # Step 3 : Separate Features and Labels
    X, Y = SeparateFeatures(df)

    # Step 4 : Split Data
    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    # Step 5 : Scale Features
    X_train, X_test, scaler = ScaleFeatures(X_train, X_test)

    # Step 6 : Create Individual Models
    model_log, model_det, model_knn = CreateModels()

    # Step 7 : Train Individual Models
    model_log, model_det, model_knn = TrainIndividualModels(
        model_log,
        model_det,
        model_knn,
        X_train,
        Y_train
    )

    # Step 8 : Evaluate Individual Models
    EvaluateIndividualModels(
        model_log,
        model_det,
        model_knn,
        X_test,
        Y_test
    )

    # Step 9 : Create Hard Voting Classifier
    model_hard = CreateHardVotingModel(
        model_log,
        model_det,
        model_knn
    )

    # Step 10 : Train Hard Voting Classifier
    model_hard = TrainVotingModel(
        model_hard,
        X_train,
        Y_train
    )

    # Step 11 : Evaluate Hard Voting Classifier
    print("Hard Voting Classifier Results : ")

    hard_accuracy = EvaluateVotingModel(
        model_hard,
        X_test,
        Y_test
    )

    # Step 12 : Create Soft Voting Classifier
    model_soft = CreateSoftVotingModel(
        model_log,
        model_det,
        model_knn
    )

    # Step 13 : Train Soft Voting Classifier
    model_soft = TrainVotingModel(
        model_soft,
        X_train,
        Y_train
    )

    # Step 14 : Evaluate Soft Voting Classifier
    print("Soft Voting Classifier Results : ")

    soft_accuracy = EvaluateVotingModel(
        model_soft,
        X_test,
        Y_test
    )

    # Step 15 : Select Best Voting Model
    if soft_accuracy >= hard_accuracy:

        best_model = model_soft

        print("Selected Model : Soft Voting Classifier")

    else:

        best_model = model_hard

        print("Selected Model : Hard Voting Classifier")

    # Step 16 : Save Model
    SaveModel(
        best_model,
        scaler,
        X.columns.tolist()
    )


if __name__ == "__main__":
    main()
