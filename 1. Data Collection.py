# First, we load the dataset into a pandas DataFrame.
import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/HR-Employee-Attrition.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
df.head()
