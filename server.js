const express = require('express');
const cors = require('cors');
const mysql = require('mysql2/promise');
const app = express();
const port = 3000;

// Configuration de la connexion à la base de données
const dbConfig = {
    host: '192.168.165.84',
    user: 'Pi',
    password: '123456',
    database: 'temp',
    port: '3306'
};

// Enable CORS for all routes
app.use(cors());

// Route pour récupérer les données
app.get('/fetch_data', async (req, res) => {
    try {
        // Connexion à la base de données
        const connection = await mysql.createConnection(dbConfig);

        // Exécution de la requête SQL
        const [rows] = await connection.execute('SELECT id, date, humidity, temperature FROM donnee');

        // Fermeture de la connexion à la base de données
        await connection.end();

        // Envoi des données au format JSON
        res.json(rows);
    } catch (error) {
        console.error('Erreur lors de la récupération des données:', error);
        res.status(500).send('Erreur serveur');
    }
});

// Démarrage du serveur
app.listen(port, () => {
    console.log(`Serveur en cours d'exécution sur le port ${port}`);
});
