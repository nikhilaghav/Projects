import numpy as np
import pandas as pd
import joblib

from pathlib import Path

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


BASE_DIR = Path(__file__).resolve().parent


#-----------------------------------------------------
#   Function Name : LoadData
#   Description :   Load dataset from CSV file
#   Input :         CSV file path
#   Output :        DataFrame
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def LoadData(DataPath):

    Border = "-" * 40

    print(Border)
    print("Step 1 : Load the data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.head())

    return df


#-----------------------------------------------------
#   Function Name : RemoveUnwantedColumns
#   Description :   Remove unnecessary columns
#   Input :         DataFrame
#   Output :        Updated DataFrame
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def RemoveUnwantedColumns(df):

    Border = "-" * 40

    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if "Unnamed: 0" in df.columns:

        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    return df


#-----------------------------------------------------
#   Function Name : CheckMissingValues
#   Description :   Check missing values in dataset
#   Input :         DataFrame
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CheckMissingValues(df):

    Border = "-" * 40

    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print(df.isnull().sum())


#-----------------------------------------------------
#   Function Name : StatisticalSummary
#   Description :   Display statistical summary
#   Input :         DataFrame
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def StatisticalSummary(df):

    Border = "-" * 40

    print(Border)
    print("Step 4 : Statistical Summary")
    print(Border)

    print(df.describe())


#-----------------------------------------------------
#   Function Name : CorrelationAnalysis
#   Description :   Display correlation matrix
#   Input :         DataFrame
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def CorrelationAnalysis(df):

    Border = "-" * 40

    print(Border)
    print("Step 5 : Correlation")
    print(Border)

    print(df.corr())


#-----------------------------------------------------
#   Function Name : SeparateFeatures
#   Description :   Separate independent and dependent
#                   variables
#   Input :         DataFrame
#   Output :        Features and target
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SeparateFeatures(df):

    Border = "-" * 40

    print(Border)
    print("Step 6 : Separate independent and dependent variables")
    print(Border)

    X = df[["TV", "radio", "newspaper"]]

    Y = df["sales"]

    print("Independent Variables : ")
    print(X.head())

    print("Dependent Variable : ")
    print(Y.head())

    return X, Y


#-----------------------------------------------------
#   Function Name : SplitData
#   Description :   Split dataset for training and testing
#   Input :         Features and target
#   Output :        Training and testing datasets
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SplitData(X, Y):

    Border = "-" * 40

    print(Border)
    print("Step 7 : Split the dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data : ", X_train.shape)
    print("Testing Data : ", X_test.shape)

    return X_train, X_test, Y_train, Y_test


#-----------------------------------------------------
#   Function Name : TrainModel
#   Description :   Create and train Linear Regression
#   Input :         Training features and target
#   Output :        Trained model
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def TrainModel(X_train, Y_train):

    Border = "-" * 40

    print(Border)
    print("Step 8 : Create & train the model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    print("Model trained successfully...")

    return model


#-----------------------------------------------------
#   Function Name : TestModel
#   Description :   Test trained regression model
#   Input :         Model and testing data
#   Output :        Predicted values
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def TestModel(model, X_test, Y_test):

    Border = "-" * 40

    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Expected answers : ")
    print(Y_test.iloc[:3])

    print("Predicted answers : ")
    print(Y_pred[:3])

    return Y_pred


#-----------------------------------------------------
#   Function Name : EvaluateModel
#   Description :   Evaluate regression model
#   Input :         Actual and predicted values
#   Output :        MSE, RMSE and R2 Score
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def EvaluateModel(Y_test, Y_pred):

    Border = "-" * 40

    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)

    RMSE = np.sqrt(MSE)

    R2 = r2_score(Y_test, Y_pred)

    print("MSE : ", MSE)
    print("RMSE : ", RMSE)
    print("R2 : ", R2)


#-----------------------------------------------------
#   Function Name : DisplayCoefficients
#   Description :   Display model coefficients
#   Input :         Trained model
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def DisplayCoefficients(model):

    Border = "-" * 40

    print(Border)
    print("Step 11 : Display Coefficients")
    print(Border)

    print("TV coefficient : ", model.coef_[0])

    print("Radio coefficient : ", model.coef_[1])

    print("Newspaper coefficient : ", model.coef_[2])

    print("Intercept : ", model.intercept_)


#-----------------------------------------------------
#   Function Name : SaveModel
#   Description :   Save trained regression model
#   Input :         Trained model
#   Output :        PKL file
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def SaveModel(model):

    Border = "-" * 40

    print(Border)
    print("Step 12 : Save the model")
    print(Border)

    joblib.dump(
        model,
        BASE_DIR / "AdvertisingSales.pkl"
    )

    print("Model saved successfully...")


#-----------------------------------------------------
#   Function Name : main
#   Description :   Entry point function
#   Input :         None
#   Output :        None
#   Author :        Nikhil Aba Aghav
#   Date :          27/10/2026
#-----------------------------------------------------

def main():

    # Step 1 : Load Dataset
    df = LoadData(BASE_DIR / "Advertising.csv")

    # Step 2 : Remove Unwanted Columns
    df = RemoveUnwantedColumns(df)

    # Step 3 : Check Missing Values
    CheckMissingValues(df)

    # Step 4 : Statistical Summary
    StatisticalSummary(df)

    # Step 5 : Correlation Analysis
    CorrelationAnalysis(df)

    # Step 6 : Separate Features and Target
    X, Y = SeparateFeatures(df)

    # Step 7 : Split Dataset
    X_train, X_test, Y_train, Y_test = SplitData(X, Y)

    # Step 8 : Train Model
    model = TrainModel(X_train, Y_train)

    # Step 9 : Test Model
    Y_pred = TestModel(model, X_test, Y_test)

    # Step 10 : Evaluate Model
    EvaluateModel(Y_test, Y_pred)

    # Step 11 : Display Coefficients
    DisplayCoefficients(model)

    # Step 12 : Save Model
    SaveModel(model)


if __name__ == "__main__":
    main()
