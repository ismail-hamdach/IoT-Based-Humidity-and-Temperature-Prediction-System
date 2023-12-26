# Humidity Prediction Model

## Description

This project focuses on building a Humidity Prediction Model using machine learning. The dataset, stored in a CSV file (`data.csv`), contains information about humidity, temperature, and date. The Python script leverages the `pandas` library for data manipulation, `scikit-learn` for machine learning, and evaluates the model's performance using Mean Absolute Error.

## Prerequisites

- Python installed on your machine
- Install required libraries using:
  ```bash
  pip install pandas scikit-learn
  ```

## Setup

1. **Install Required Python Libraries:**
   ```bash
   pip install pandas scikit-learn
   ```

2. **Prepare the Dataset:**
   - Ensure you have a CSV file named `data.csv` with columns: `id`, `date`, `humidity`, `temperature`.

3. **Run the Script:**
   - Execute the Python script to load, preprocess the data, train the model, and make predictions:
     ```bash
     python main.py
     ```
     Replace `main.py` with the actual name of your Python script.

## Project Structure

- `main.py`: The main Python script for loading data, preprocessing, training the model, and making predictions.
- `data.csv`: CSV file containing the dataset.

## Steps Overview

1. **Load and Display Data:**
   - Load the dataset from `data.csv` using `pandas` and display the initial data.

2. **Data Preprocessing:**
   - Convert the 'date' column to datetime format.
   - Extract 'year', 'month', and 'day' features from the 'date' column.

3. **Train-Test Split:**
   - Split the dataset into training and testing sets.

4. **Model Selection and Training:**
   - Use a Linear Regression model to predict humidity based on year, month, day, and temperature.

5. **Model Evaluation:**
   - Assess the model's performance using Mean Absolute Error (MAE).

6. **Prediction:**
   - Make a sample prediction for a given set of features (year, month, day, temperature).

## Notes

- Ensure the CSV file (`data.csv`) is correctly formatted with the required columns.
- Adjust the script as needed for your specific use case and dataset.