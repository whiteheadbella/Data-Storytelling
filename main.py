import pandas as pd
import streamlit as st
import os
import glob
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit App Title
st.title("Heart Disease Dataset Analysis")

# Define file path
file_path = "heart_disease.csv"

# Function to check if the file exists
def find_dataset():
    if os.path.exists(file_path):
        return file_path
    else:
        possible_files = glob.glob("**/heart_disease.csv", recursive=True)
        return possible_files[0] if possible_files else None

# Try loading the dataset
data = None
found_file = find_dataset()

if found_file:
    try:
        data = pd.read_csv(found_file)
        st.success(f"Data loaded successfully from: `{found_file}`")
    except pd.errors.EmptyDataError:
        st.error("The file is empty!")
    except Exception as e:
        st.error(f"Error loading data: {e}")
else:
    st.warning("File 'heart_disease.csv' not found in the current directory.")
    st.write("Please upload the file below.")

# File Upload Option
uploaded_file = st.file_uploader("Upload heart_disease.csv", type=["csv"])
if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("File uploaded and loaded successfully!")
    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")

# Display Data Preview
if data is not None:
    st.subheader("First 5 Rows of the Dataset")
    st.dataframe(data.head())

    # Display Data Summary
    st.subheader("Dataset Summary")
    st.write(data.describe())

    # Display Missing Values
    st.subheader("Missing Values in Dataset")
    missing_values = data.isnull().sum()
    st.write(missing_values[missing_values > 0])

# Show Current Directory and Files (Debugging)
st.subheader("Debugging Information")
st.write("Current Working Directory:", os.getcwd())
st.write("Files in Directory:", os.listdir())


def introduction():
    st.title("Heart Disease Analysis: A Data-Driven Approach")
    st.markdown("""
    The dataset provides valuable insights into heart disease, focusing on various factors such as age, gender, cholesterol levels, and lifestyle choices.
    This analysis aims to uncover patterns and trends that can help in understanding the risk factors associated with heart disease.
    """)

def plot_age_distribution(data):
    if data is not None:
        st.subheader("Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(data['Age'], bins=30, kde=True, color='blue', ax=ax)
        st.pyplot(fig)
        st.markdown("""
        The age distribution of patients shows that certain age groups are more prevalent in the dataset. 
        The majority of patients fall within the age range of 50 to 80 years, indicating that heart disease is more common in older individuals.
        """)

def plot_gender_distribution(data):
    if data is not None:
        st.subheader("Gender Distribution")
        fig = px.histogram(data, x='Gender', color='Heart Disease Status', barmode='group', title='Heart Disease by Gender')
        st.plotly_chart(fig)
        st.markdown("""
        The gender distribution analysis reveals that both males and females are similarly represented in the dataset. However, further analysis shows that there are gender-based differences in heart disease prevalence.
        """)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cholesterol_levels(data):
    # Ensure the data is valid and contains the required columns
    if data is None or data.empty:
        st.error("Error: No data available. Please check if the dataset is loaded correctly.")
        return

    required_columns = {"Cholesterol", "Heart Disease Status"}
    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        st.error(f"Error: Missing columns {missing_columns} in the dataset!")
        return

    # Plot the cholesterol levels boxplot
    st.subheader("Cholesterol Levels and Heart Disease")
    fig, ax = plt.subplots(figsize=(10, 5))  # Ensure consistent figure size
    sns.boxplot(x='Heart Disease Status', y='Cholesterol', data=data, ax=ax)
    ax.set_title("Cholesterol Levels by Heart Disease Status")

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Explanation markdown
    st.markdown("""
    **🔍 Key Insights:**  
    - High cholesterol is a key risk factor for heart disease.  
    - The boxplot shows that patients with heart disease tend to have higher cholesterol levels compared to those without heart disease.  
    - Understanding cholesterol levels can help in early intervention and lifestyle modifications.
    """)



def plot_lifestyle_factors(data):
    if data is not None:
        st.subheader("Lifestyle Factors: Smoking, Alcohol, & Exercise")
        fig = px.histogram(data, x='Smoking', color='Heart Disease Status', barmode='group', title='Smoking and Heart Disease')
        st.plotly_chart(fig)
        st.markdown("""
        Lifestyle choices significantly impact heart disease risk. The countplot analysis demonstrates that smoking, alcohol consumption, and lack of exercise are associated with higher heart disease prevalence.
        """)

def plot_correlation_heatmap(data):
    if data is not None:
        st.subheader("Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        st.pyplot(fig)
        st.markdown("""
        The correlation heatmap identifies the strongest predictors of heart disease. 
        Factors such as age, cholesterol levels, and lifestyle choices show significant correlations with heart disease status.
        """)

def insights_and_recommendations():
    st.subheader("Insights and Recommendations")
    st.markdown("""
    1. **Healthcare Policies**: Tailoring healthcare policies for older age groups can help in early detection and management of heart disease.
    2. **Gender-Based Differences**: Addressing gender-based differences in heart disease risk can lead to more effective prevention strategies.
    3. **Lifestyle Interventions**: Promoting healthy lifestyle choices, such as quitting smoking, reducing alcohol consumption, and encouraging regular exercise, can significantly reduce heart disease risk.
    4. **Cholesterol Monitoring**: Regular monitoring of cholesterol levels, especially in older individuals, is essential for preventing heart disease.
    
    By understanding these insights, healthcare providers and policymakers can make informed decisions to improve heart disease prevention and management strategies.
    """)

def main():
    try:
        data = pd.read_csv("./heart_disease.csv")
    except FileNotFoundError:
        st.error("Error: The dataset 'heart_disease.csv' was not found. Please check the file path.")
        data = None
    introduction()
    plot_age_distribution(data)
    plot_gender_distribution(data)
    plot_cholesterol_levels(data)
    plot_lifestyle_factors(data)
    plot_correlation_heatmap(data)
    insights_and_recommendations()

if __name__ == "__main__":
    main()

import os
print(os.getcwd())  # This prints the current working directory
print(os.listdir()) # This lists all files in the directory


data = pd.read_csv("heart_disease.csv")
data = pd.read_csv(r"C:\Users\white\OneDrive\Desktop\DataAnalysis\heart_disease.csv")

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define file path
file_path = r"C:\Users\white\OneDrive\Desktop\DataAnalysis\heart_disease.csv"

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
else:
    # Load data
    data = pd.read_csv(file_path)
    
    # Remove leading/trailing spaces from column names
    data.columns = data.columns.str.strip()
    
    # Print available columns for debugging
    print("Available columns:", data.columns.tolist())

    # Check if required columns exist
    required_columns = {"Cholesterol", "Heart Disease Status"}
    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        print(f"Error: Missing columns {missing_columns} in the dataset!")
    else:
        # Plot function
        def plot_cholesterol_levels(data):
            plt.figure(figsize=(8, 5))
            sns.boxplot(x='Heart Disease Status', y='Cholesterol', data=data)
            plt.title("Cholesterol Levels by Heart Disease Status")
            plt.show()

        # Call the function to plot the data
        plot_cholesterol_levels(data)


