document.addEventListener("DOMContentLoaded", function() {
const startDateInput = document.getElementById('startDate');
const endDateInput = document.getElementById('endDate');
const inputContainer = document.getElementById('inputContainer');
const includedContainer = document.getElementById('includedContainer');
let includedFields = []; // Initialize includedFields array

function createInputs() {
    const startDate = new Date(startDateInput.value);
    const endDate = new Date(endDateInput.value);
    const oneDayInMilliseconds = 24 * 60 * 60 * 1000;
    const diffDays = Math.round(Math.abs((endDate - startDate) / oneDayInMilliseconds));

    function no_of_day() {
    document.getElementById('no_of_day').value = diffDays + 1;
    }

    no_of_day();
    inputContainer.innerHTML = '';
    for (let i = 0; i < diffDays + 1; i++) {
    const input = document.createElement('input');
    input.type = 'text';
    input.name = `day_${i + 1}`;
    input.placeholder = `Day ${i + 1}`;
    input.required = true;
    inputContainer.appendChild(input);
    }
}

function addIncludedField() {
    const newField = document.createElement('div');
    newField.className = 'row x-gap-20 y-gap-20 included-field';

    const fieldName = document.createElement('input');
    fieldName.type = 'text';
    fieldName.className = 'form-control included-name';
    fieldName.placeholder = 'Field Name';
    fieldName.required = true;

    const deleteButton = document.createElement('button');
    deleteButton.type = 'button';
    deleteButton.className = 'btn btn-danger delete-button';
    deleteButton.innerHTML = 'Delete';
    deleteButton.addEventListener('click', function() {
    includedContainer.removeChild(newField);
    updateIncludedJson();
    });

    newField.appendChild(fieldName);
    newField.appendChild(deleteButton);

    includedContainer.appendChild(newField);
    includedFields.push(newField);
    updateIncludedJson();
}

function updateIncludedJson() {
    const includedData = {};
    includedFields.forEach((field, index) => {
    const fieldName = field.querySelector('.included-name').value;
    includedData[index + 1] = fieldName;
    });

    document.getElementById('includedJson').value = JSON.stringify(includedData);
}

startDateInput.addEventListener('change', createInputs);
endDateInput.addEventListener('change', createInputs);

document.getElementById('new_tour_form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission to allow processing
    const inputs = inputContainer.querySelectorAll('input');
    const data = {};
    inputs.forEach(input => {
    data[input.name] = input.value;
    });
    document.getElementById('itineraryJson').value = JSON.stringify(data);
    const jsdata = JSON.stringify(data);
    console.log(jsdata);

    // Ensure included fields are processed
    updateIncludedJson();
    const includedJson = document.getElementById('includedJson').value;
    console.log(includedJson);

    // Submit the form programmatically if needed
    // this.submit();
});


// Calendar validation
const today = new Date().toISOString().split('T')[0];
document.getElementById('startDate').setAttribute('min', today);
document.getElementById('endDate').setAttribute('min', today);
});
