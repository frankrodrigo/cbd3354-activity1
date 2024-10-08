// Simple form validation and dynamic table update
document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting

    // Get form field values
    const username = document.getElementById('username').value.trim();
    const cellphone = document.getElementById('cellphone').value.trim();
    let isValid = true;

    // Simple validation for empty fields and valid phone number (basic regex)
    if (username === '') {
        document.getElementById('usernameError').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('usernameError').style.display = 'none';
    }

    const phoneRegex = /^[0-9]{10}$/; // Simple regex for a 10-digit number
    if (cellphone === '' || !phoneRegex.test(cellphone)) {
        document.getElementById('cellphoneError').style.display = 'block';
        isValid = false;
    } else {
        document.getElementById('cellphoneError').style.display = 'none';
    }

    // If valid, insert user data into the table
    if (isValid) {
        const table = document.getElementById('userTable').getElementsByTagName('tbody')[0];
        const newRow = table.insertRow();

        const usernameCell = newRow.insertCell(0);
        const cellphoneCell = newRow.insertCell(1);

        usernameCell.textContent = username;
        cellphoneCell.textContent = cellphone;

        // Clear form fields after successful submission
        document.getElementById('username').value = '';
        document.getElementById('cellphone').value = '';
    }
});
