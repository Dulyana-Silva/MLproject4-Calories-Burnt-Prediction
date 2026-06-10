# Calories Burnt Prediction

## Project Overview

This project focuses on predicting the number of calories burned during physical activity using Machine Learning. The model was trained on physiological and exercise-related attributes. The project demonstrates an end-to-end Machine Learning workflow, from raw data analysis to model deployment and was successfully integrated into a Streamlit application, providing users with real-time calorie burn predictions.

---

## Objectives

* Analyze factors that influence calorie expenditure.
* Build a predictive machine learning model for calorie burn estimation.
* Evaluate model performance using appropriate regression metrics.
* Deploy the trained model as an interactive web application.

---

## Technologies Used

### Programming Language

* Python

### Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Streamlit
* Pickle

---

## About Dataset

The dataset contains information related to individual physical characteristics and workout conditions. (Concatination of 2 datasets)

### Features

* Gender
* Age
* Height
* Weight
* Duration
* Heart Rate
* Body Temperature

### Target Variable

* Calories Burned

---

## Project Workflow

### 1. Importing Dependencies

The project begins by importing the required libraries for:

* Data manipulation
* Data visualization
* Machine learning
* Model evaluation

### 2. Data Collection

The dataset was loaded into a Pandas DataFrame and inspected for:

* Shape
* Data types
* Missing values
* Statistical summaries

### 3. Data Preprocessing

The preprocessing stage involved:

* Checking for missing values
* Verifying data consistency
* Preparing data for machine learning

### 4. Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and identify patterns.

Key activities included:

* Distribution analysis
* Feature relationship analysis
* Outlier inspection
* Understanding target variable behavior

### 5. Data Visualization

Several visualizations were created using Matplotlib and Seaborn including:

* Histograms
* Count plots
* Correlation heatmaps
* Residual plots

These visualizations helped reveal relationships between variables and calories burned.

### 6. Correlation Analysis

A correlation matrix was generated to identify the strength of relationships among variables.
Insights from correlation analysis helped understand which features were most influential in predicting calorie expenditure.

### 7. Encoding Categorical Variables

The Gender feature was converted into numerical format:

* Male = 0
* Female = 1

This allowed the machine learning algorithm to process the categorical feature.

### 8. Feature and Target Separation

The dataset was divided into:

#### Features (X)

* Gender
* Age
* Height
* Weight
* Duration
* Heart Rate
* Body Temperature

#### Target (Y)

* Calories Burned

### 9. Train-Test Split

The dataset was divided into:

* Training Set (80%)
* Testing Set (20%)

This ensured unbiased model evaluation.

### 10. Model Training

An XGBoost Regression model was selected due to its strong predictive performance and ability to handle complex relationships within data.

The model was trained using:

```python
from xgboost import XGBRegressor

model = XGBRegressor()
model.fit(X_train, Y_train)
```

### 11. Model Evaluation

The model was evaluated using Mean Absolute Error (MAE).

#### Results

* MAE = 1.4833
This indicates that the model's predictions differ from the actual calorie values by approximately 1.48 calories on average.
The low error demonstrates strong predictive performance.

* R² = 0.9988
Since R² > 0.98 → The model is Outstanding.

### 12. Residual Analysis

Residual analysis was performed to assess prediction quality.

Residual plots were used to:

* Detect prediction bias
* Identify unusual observations
* Verify model reliability

A random residual pattern around zero suggests that the model successfully captured the underlying relationships in the data.

---

## Model Deployment

The trained model was serialized using Pickle and integrated into a Streamlit web application.

The application allows users to enter:

* Gender
* Age
* Height
* Weight
* Workout Duration
* Heart Rate
* Body Temperature

The model then predicts the estimated calories burned in real time.

---

## Streamlit Application Features

* Interactive user interface
* Real-time calorie prediction
* User-friendly design
* Machine Learning powered recommendations

### Click the Link to view the streamlit app -  
https://mlproject4-calories-burnt-prediction-kyufafihyr765k4njuthri.streamlit.app/

<p align = "center"><img width="537" height="773" alt="image" src="https://github.com/user-attachments/assets/36889d87-0209-46af-86f4-25d2abf7dd30" /><p/>

---

## Future Improvements

* Add BMI calculation
* Add fitness recommendations
* Deploy using cloud infrastructure
* Develop a mobile application version
