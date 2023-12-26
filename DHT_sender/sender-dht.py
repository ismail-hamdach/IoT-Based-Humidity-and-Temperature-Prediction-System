import Adafruit_DHT
import time
import mysql.connector

sensor = Adafruit_DHT.DHT22
pin = 4  # GPIO pin where the data line is connected

# MySQL Database Configuration
db_config = {
    'user': 'Pi',
    'password': '123456',
    'host': '192.168.243.84',
    'database': 'temp',
    'port': 3306  # Default MySQL port
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