# IoT Temperature and Humidity Logger

## Description

This project utilizes a Raspberry Pi, a DHT22 sensor, and a MySQL database to create a simple yet effective IoT Temperature and Humidity Logger. The script continuously reads data from the sensor and stores it in a MySQL database. It incorporates environment variables for configuration, making it easy to customize the GPIO pin, MySQL credentials, and other settings.

## Prerequisites

Before running the script, ensure the following:

- Raspberry Pi with GPIO pins
- DHT22 sensor connected to the appropriate GPIO pin
- Python installed on the Raspberry Pi
- MySQL server accessible from the Raspberry Pi
- `python-dotenv` library installed (`pip install python-dotenv`)

## Setup

1. **Connect the Hardware:**
   - Connect the DHT22 sensor to the GPIO 4 pin on your Raspberry Pi. Adjust the `GPIO_PIN` variable in the `.env` file if using a different pin.

2. **Install Required Python Libraries:**
   ```bash
   pip install Adafruit_DHT mysql-connector-python python-dotenv
   ```

3. **Create a MySQL Database:**
   - Create a MySQL database and table to store temperature and humidity data. Modify the database configuration in the `.env` file accordingly.

4. **Configure Environment Variables:**
   - Create a `.env` file in the same directory as your script with the following content:
     ```env
     GPIO_PIN=your_gpio_pin
     DB_USER=your_database_user
     DB_PASSWORD=your_database_password
     DB_HOST=your_database_host
     DB_DATABASE=your_database_name
     DB_PORT=your_database_port
     ```

5. **Run the Script:**
   - Execute the Python script to start logging data:
     ```bash
     python sender-dht.py
     ```
     Replace `sender-dht.py` with the actual name of your Python script.

## Project Structure

- `sender-dht.py`: The main Python script for reading sensor data and storing it in the MySQL database.
- `.env`: Configuration file containing environment variables for GPIO pin, database credentials, etc.

## Notes

- Make sure the Raspberry Pi has internet access to install required Python libraries.
- Adjust the script and database configurations as needed for your specific setup.
