# Wine-Quality-Predictor

This project predicts the quality of red wine based on various physicochemical properties using different machine learning models.
It also compares model performance and visualizes feature importances and results.


Overview

The goal of this project is to build and evaluate multiple classification models to predict wine quality (good vs. bad or multi-class quality scores) from the winequality-red.csv dataset.
Through exploratory data analysis (EDA) and model evaluation, we identify the best-performing algorithm for this dataset.


Dataset Features
	•	fixed acidity
	•	volatile acidity
	•	citric acid
	•	residual sugar
	•	chlorides
	•	free sulfur dioxide
	•	total sulfur dioxide
	•	density
	•	pH
	•	sulphates
	•	alcohol
	•	Target: quality (wine quality score from 0–10)


Models Used

The notebook compares several models:
	•	Logistic Regression
	•	K-Nearest Neighbors (KNN)
	•	Support Vector Classifier (SVC)
	•	Decision Tree Classifier
	•	Random Forest Classifier
	•	XGBoost Classifier


Tech Stack
	•	Language: Python 3
	•	Libraries:
	•	Data Handling: pandas, numpy
	•	Visualization: matplotlib, seaborn
 
