import Adafruit_DHT
import time
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

sensor = Adafruit_DHT.DHT22
pin = int(os.getenv('GPIO_PIN', 4))  # GPIO pin where the data line is connected

# MySQL Database Configuration
db_config = {
    'user': os.getenv('DB_USER', 'Pi'),  # Use the environment variable if set, otherwise use a default value
    'password': os.getenv('DB_PASSWORD', '123456'),  # Use the environment variable if set, otherwise use a default value
    'host': os.getenv('DB_HOST', '192.168.243.84'),  # Use the environment variable if set, otherwise use a default value
    'database': os.getenv('DB_DATABASE', 'temp'),  # Use the environment variable if set, otherwise use a default value
    'port': int(os.getenv('DB_PORT', 3306))  # Use the environment variable if set, otherwise use a default value
}

try:
    # Connect to the MySQL server
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            # Insert data into the database
            query = "INSERT INTO donnee (temperature, humidity) VALUES (%s, %s)"
            data = (temperature, humidity)
            cursor.execute(query, data)
            conn.commit()

            print(f'Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}% - Data saved to the database')

        else:
            print('Failed to retrieve data from the sensor')

        time.sleep(2)  # wait for 2 seconds before the next reading

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the database connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
