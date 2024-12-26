"""
Now, we will evaluate the models using various classification metrics such as Accuracy,
Precision, Recall, and F1-Score.
"""

# Evaluate Logistic Regression Model
print("Logistic Regression:")
print(classification_report(y_test, log_reg_pred))

# Evaluate Random Forest Model
print("Random Forest:")
print(classification_report(y_test, rf_pred))

# Evaluate XGBoost Model
print("XGBoost:")
print(classification_report(y_test, xgb_pred))
