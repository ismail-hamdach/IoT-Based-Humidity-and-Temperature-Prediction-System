import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

def load_data(file_path):
    # Load data from CSV
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # Data preprocessing
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df[['year', 'month', 'day', 'temperature']], df['humidity']

def split_data(X, y):
    # Train-Test Split
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    # Model Selection and Training
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    # Model Evaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae}')

def make_prediction(model, new_data):
    # Prediction
    prediction = model.predict(new_data)
    print(f'Predicted Humidity: {prediction[0]}')

if __name__ == "__main__":
    # Step 1: Load Data
    file_path = 'data.csv'
    df = load_data(file_path)

    # Step 2: Data Preprocessing
    X, y = preprocess_data(df)

    # Step 3: Train-Test Split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Step 4: Model Training
    model = train_model(X_train, y_train)

    # Step 5: Model Evaluation
    evaluate_model(model, X_test, y_test)

    # Step 6: Prediction
    new_data_1 = pd.DataFrame({'year': [2023], 'month': [12], 'day': [30], 'temperature': [22]})
    make_prediction(model, new_data_1)

    new_data_2 = pd.DataFrame({'year': [2023], 'month': [1], 'day': [1], 'temperature': [25]})
    make_prediction(model, new_data_2)
