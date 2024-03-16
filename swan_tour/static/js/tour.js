const startDateInput = document.getElementById('startDate');
const endDateInput = document.getElementById('endDate');
const inputContainer = document.getElementById('itineraryInputContainer');

function createInputs() {
  const startDate = new Date(startDateInput.value);
  const endDate = new Date(endDateInput.value);
  const oneDayInMilliseconds =  24 *  60 *  60 *  1000;
  const diffDays = Math.round(Math.abs((endDate - startDate) / oneDayInMilliseconds));

  inputContainer.innerHTML = '';

  for (let i =  0; i < diffDays; i++) {
    const input = document.createElement('input');
    input.type = 'text';
    input.name = `itinerary_${i +  1}`;
    input.placeholder = `Day ${i +  1}`;
    input.required = true;
    inputContainer.appendChild(input);
  }
}

startDateInput.addEventListener('change', createInputs);
endDateInput.addEventListener('change', createInputs);

document.getElementById('yourFormId').addEventListener('submit', function(event) {
  const inputs = inputContainer.querySelectorAll('input');
  const data = {};
  inputs.forEach(input => {
    data[input.name] = input.value;
  });
  document.getElementById('itineraryJson').value = JSON.stringify(data);
});