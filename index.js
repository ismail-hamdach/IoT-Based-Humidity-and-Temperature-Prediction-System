document.addEventListener("DOMContentLoaded", function () {
    // Initialize page and items per page
    let currentPage = 1;
    const itemsPerPage = 10; // Adjust this based on your preference

    // Call the function to fetch data from the server
    fetchData(currentPage, itemsPerPage);
});

function fetchData(page, itemsPerPage) {
    // Display loading effect
    const tableContainer = document.getElementById('table-container');
    tableContainer.innerHTML = '<p>Loading...</p>';

    // Use an AJAX request to fetch data from the server
    const serverUrl = window.config.SERVER_URL; // Use the environment variable if set, otherwise use a default value
    fetch(`${serverUrl}/fetch_data?page=${page}&itemsPerPage=${itemsPerPage}`)
        .then(response => {
            if (!response.ok) {
                tableContainer.innerHTML = `<p class="error" >Network response was not ok: ${response.status}</p>`;
                throw new Error(`Network response was not ok: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Call the function to display data in the table
            displayData(data);
        })
        .catch(error => {
            // Display error message
            tableContainer.innerHTML = `<p>Error fetching data: ${error.message}</p>`;
            console.error('Error fetching data:', error);
        });
}

function displayData(data) {
    // Create the table
    const tableContainer = document.getElementById('table-container');
    tableContainer.innerHTML = ''; // Clear the existing content

    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const tbody = document.createElement('tbody');

    // Create the table header
    const headers = ['ID', 'Date', 'Humidity', 'Temperature'];
    const headerRow = document.createElement('tr');
    headers.forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Fill the table with data
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

// Add pagination controls (customize based on your UI)
function changePage(newPage) {
    const itemsPerPage = 10; // Adjust this based on your preference
    fetchData(newPage, itemsPerPage);
}
