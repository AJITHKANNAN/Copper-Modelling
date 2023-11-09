# Copper-Modelling

**Data Exploration:**
Load the dataset and explore it to understand its structure and features.
Analyze the distribution of the target variable (Selling_Price) to identify skewness.
Identify and visualize outliers in the dataset.

**Data Pre-processing:**

Handle missing values if any.
Apply data normalization and feature scaling techniques to address skewness and ensure that features are on a similar scale.
Address outliers by either removing them or applying appropriate transformations.

**Regression Model:**

Split the dataset into training and testing sets.
Choose and implement a regression algorithm (e.g., Linear Regression, Random Forest Regression).
Train the model on the training set and evaluate its performance on the testing set.
Fine-tune hyperparameters if needed.

**Classification Model:**

Create a binary classification target variable based on the STATUS column, where 'WON' is considered as Success (1) and 'LOST' as Failure (0).
Split the dataset into training and testing sets.
Choose and implement a classification algorithm (e.g., Logistic Regression, Random Forest Classification).
Train the model on the training set and evaluate its performance on the testing set.
Fine-tune hyperparameters if needed.

**Streamlit Application:**

Create a Streamlit web application.
Design an interface where users can input values for each column.
Implement the regression model to predict Selling_Price based on the input values.
Implement the classification model to predict the lead status ('WON' or 'LOST') based on the input values.
Display the predicted values on the Streamlit page.

**Testing and Validation:**

Test the models with different inputs to ensure accurate predictions.
Validate the models using metrics appropriate for regression (e.g., Mean Absolute Error) and classification (e.g., Accuracy, Precision, Recall).

**Documentation:**

Document the steps taken, choices made (e.g., algorithms used, hyperparameters), and the reasoning behind them.
Provide instructions on how to run and use the Streamlit application.

Remember to iterate on these steps as needed and continuously improve the models based on feedback and performance metrics

Note:
I haven't uploaded the pickle files since it crossed more than 2.5 GB, I will try to Zip it an upload it 
