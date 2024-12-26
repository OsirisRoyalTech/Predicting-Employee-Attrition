"""
We will clean the dataset, handle missing values, encode categorical variables, and
prepare the features and target variable for modeling.
"""

# Check for missing values
df.isnull().sum()

# Drop the 'EmployeeCount' and 'Over18' columns as they do not provide useful information
df.drop(['EmployeeCount', 'Over18'], axis=1, inplace=True)

# Convert categorical variables to numerical (if needed)
df = pd.get_dummies(df, drop_first=True)

# Encode the target variable (Attrition) to 0 (No) and 1 (Yes)
df['Attrition'] = df['Attrition'].map({'No': 0, 'Yes': 1})

# Separate features and target variable
X = df.drop('Attrition', axis=1)  # Features
y = df['Attrition']  # Target variable (Attrition: 1, No Attrition: 0)
