require('dotenv').config({ debug: true });

const express = require('express');
const cors = require('cors');
const mysql = require('mysql2/promise');
const app = express();

const port = process.env.PORT || 3000; // Use the environment variable

// Database connection configuration
const dbConfig = {
    host: process.env.DB_HOST , // Use the environment variable
    user: process.env.DB_USER , // Use the environment variable
    password: process.env.DB_PASSWORD , // Use the environment variable
    database: process.env.DB_DATABASE , // Use the environment variable
    port: process.env.DB_PORT // Use the environment variable
};

// Enable CORS for all routes
app.use(cors());

// Route to fetch data
app.get('/fetch_data', async (req, res) => {
    try {
        // Connect to the database
        const connection = await mysql.createConnection(dbConfig);

        // Execute the SQL query
        const [rows] = await connection.execute(`SELECT id, date, humidity, temperature FROM ${process.env.DB_TABLE}`);

        // Close the database connection
        await connection.end();

        // Send data in JSON format
        res.json(rows);
    } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).send('Server error');
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
