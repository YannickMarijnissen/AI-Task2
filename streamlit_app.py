import subprocess
import sys
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install_package("pandas")
install_package("streamlit")
install_package("scikit-learn")

# Load the dataset with space as the delimiter
file_path = 'rocket_league_skillshots.data'
df = pd.read_csv(file_path, delimiter=' ', header=None)

# Display the data
st.dataframe(df)

# Button to calculate accuracy
if st.button('Calculate Accuracy'):
    # Check if the dataset has numeric values
    if df.applymap(lambda x: pd.to_numeric(x, errors='coerce')).notna().all().all():
        # If numeric, split the data
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        # Split the data into a training set and a test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train a RandomForestClassifier
        random_forest_model = RandomForestClassifier(random_state=42)
        random_forest_model.fit(X_train, y_train)

        # Make predictions on the test data
        y_pred_rf = random_forest_model.predict(X_test)

        # Calculate the accuracy of the RandomForest model
        accuracy_rf = accuracy_score(y_test, y_pred_rf)

        # Display the model accuracy
        st.write("Random Forest Model Accuracy:", accuracy_rf)
    else:
        # If not numeric, encode categorical variables
        label_encoder = LabelEncoder()
        df_encoded = df.apply(lambda col: label_encoder.fit_transform(col.astype(str)))

        # Split the data into a training set and a test set
        X_train, X_test, y_train, y_test = train_test_split(df_encoded.iloc[:, :-1], df_encoded.iloc[:, -1], test_size=0.2, random_state=42)

        # Create and train a RandomForestClassifier
        random_forest_model = RandomForestClassifier(random_state=42)
        random_forest_model.fit(X_train, y_train)

        # Make predictions on the test data
        y_pred_rf = random_forest_model.predict(X_test)

        # Calculate the accuracy of the RandomForest model
        accuracy_rf = accuracy_score(y_test, y_pred_rf)

        # Display the model accuracy
        st.write("Random Forest Model Accuracy:", accuracy_rf)
