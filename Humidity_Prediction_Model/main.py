import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# load data from csv
df = pd.read_csv('data.csv')
# print head of df
df.head()


# We use DataFrame with columns: id, date, humidity, temperature
# Step 1: Data Preprocessing
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

X = df[['year', 'month', 'day', 'temperature']]
y = df['humidity']

df.head()

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Selection and Training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Step 5: Prediction
new_data = pd.DataFrame({'year': [2023], 'month': [12], 'day': [30], 'temperature': [22]})
prediction = model.predict(new_data)
print(f'Predicted Humidity: {prediction[0]}')

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Selection and Training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Step 5: Prediction
new_data = pd.DataFrame({'year': [2023], 'month': [1], 'day': [1], 'temperature': [25]})
prediction = model.predict(new_data)
print(f'Predicted Humidity: {prediction[0]}')