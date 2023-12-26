document.addEventListener("DOMContentLoaded", function () {
    // Initialize page and items per page
    let currentPage = 1;
    const itemsPerPage = 10; // Adjust this based on your preference

    // Appel de la fonction pour récupérer les données depuis le serveur
    fetchData(currentPage, itemsPerPage);
});

function fetchData(page, itemsPerPage) {
    // Utiliser une requête AJAX pour récupérer les données depuis le serveur
    // Ici, vous pourriez utiliser Fetch API ou XMLHttpRequest

    // Exemple avec Fetch API
    fetch(`http://localhost:3000/fetch_data?page=${page}&itemsPerPage=${itemsPerPage}`)
        .then(response => response.json())
        .then(data => {
            // Appel de la fonction pour afficher les données dans le tableau
            displayData(data);
        })
        .catch(error => console.error('Erreur lors de la récupération des données:', error));
}

function displayData(data) {
    // Création du tableau
    const tableContainer = document.getElementById('table-container');
    tableContainer.innerHTML = ''; // Clear the existing content

    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    // Création de l'en-tête du tableau
    const headers = ['ID', 'Date', 'Humidity', 'Temperature'];
    const headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Remplissage du tableau avec les données
    data.forEach(rowData => {
        const row = document.createElement('tr');
        Object.values(rowData).forEach(value => {
            const td = document.createElement('td');
            td.textContent = value;
            row.appendChild(td);
        });
        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    tableContainer.appendChild(table);
}

// Add pagination controls (you can customize this based on your UI)
function changePage(newPage) {
    const itemsPerPage = 10; // Adjust this based on your preference
    fetchData(newPage, itemsPerPage);
}
