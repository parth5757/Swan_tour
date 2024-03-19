// Function to convert date from "Month dd, yyyy" format to "mm/dd/yyyy" format
document.addEventListener('DOMContentLoaded', function() {
    const decrementButton = document.querySelector('.decrement');
    const incrementButton = document.querySelector('.increment');
    const countElement = document.querySelector('.count');
    const count1Element = document.querySelector('.count1');
    const count2Element = document.querySelector('.count2');
    const adultsContainer = document.getElementById('adults-container');
    const start_date = document.getElementById('start_date');
    const end_date = document.getElementById('end_date');
    const amountElement = document.querySelector('.final_amount');
    const amount1Element = document.querySelector('.final_amount1');
    const hidden_no_of_peopleElement = document.getElementById('hidden_no_of_people');
    const hidden_total_priceElement = document.getElementById('hidden_total_price');

    let count =  {{no_of_people_booking}}; // Initialize count to  1 as per your requirement

    decrementButton.addEventListener('click', () => {
        if (count >  1) { // Ensure the count does not go below  1
            count--;
            updateCount();
            removeInputFields();
        }
    });

    incrementButton.addEventListener('click', () => {
        if (count < {{ tour.get_available_group_size }}) {
            count++;
            updateCount();
            addInputFields();
        }
    });

    function addInputFields() {
        const inputGroup = document.createElement('div');
        inputGroup.innerHTML = `
            {{ formset.management_form }}
            {% for form in formset %}
                {{ form }}
            {% endfor %}
        `;
        adultsContainer.appendChild(inputGroup);
    }

    function removeInputFields() {
        if (adultsContainer.children.length >  0) {
            adultsContainer.removeChild(adultsContainer.lastChild);
        }
    }

    function updateCount() {
        countElement.textContent = count;
        count1Element.textContent = count;
        count2Element.textContent = count;
        hidden_no_of_peopleElement.value = count;
        let final_amount = count * {{ tour.total_price }};
        final_amount.textContent = final_amount;
        amountElement.textContent = final_amount;
        amount1Element.textContent = final_amount
        hidden_total_priceElement.value = final_amount;
    }

    function update_hidden_fields() {
        final_amount = {{no_of_people_booking}} * {{ tour.total_price }};
        hidden_total_priceElement.value = final_amount;
    }


    // this work fine
    function update(){
        let final_amount = {{no_of_people_booking}} * {{ tour.total_price }};
        final_amount.textContent = final_amount;
        amountElement.textContent = final_amount;
    }
    
    function update_input_field() {
        for (let i = 0; i <= {{no_of_people_booking}}-2; i++) {
            addInputFields();
        }
    }


    function on_load(){
        update_input_field();
        update();
        update_hidden_fields();
    }

    window.onload = on_load();
});