document.addEventListener("DOMContentLoaded", function() {
    var editButton = document.getElementById('editButton');
    editButton.addEventListener('click', function() {
        var orderId = this.getAttribute('data-order-id');
        
        // Make an AJAX request to fetch order data based on the orderId
        fetch(`/api/order/${orderId}`)
            .then(response => response.json())
            .then(orderData => {
                // Populate fields in the edit modal with orderData
                populateEditModal(orderData);
                
                // Show the edit modal
                $('#editModal').modal('show');
            })
            .catch(error => {
                console.error('Error fetching order data:', error);
            });
    });
});

function populateAllergiesList(allergies, allergies_options) {
    var ul = document.getElementById('allergiesList');
    ul.innerHTML = ''; // Clear existing list items
    for (var i = 0; i < allergies_options.length; i++) {
        var li = document.createElement('li');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = 'allergies';
        checkbox.value = allergies_options[i];
        // Check if the current allergy option exists in the allergies array
        if (allergies.includes(allergies_options[i])) {
            checkbox.checked = true; // Mark the checkbox as checked
        }
        var label = document.createElement('label');
        label.textContent = allergies_options[i];
        li.appendChild(checkbox);
        li.appendChild(label);
        ul.appendChild(li);
    }
}

function populateDiateryList(dietary_restriction, dietary_restriction_options) {
    var ul = document.getElementById('dietaryList');
    ul.innerHTML = ''; // Clear existing list items
    for (var i = 0; i < dietary_restriction_options.length; i++) {
        var li = document.createElement('li');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.name = 'dietary_restriction';
        checkbox.value = dietary_restriction_options[i];
        if (dietary_restriction.includes(dietary_restriction_options[i])) {
            checkbox.checked = true;
        }
        var label = document.createElement('label');
        label.textContent = dietary_restriction_options[i];
        li.appendChild(checkbox);
        li.appendChild(label);
        ul.appendChild(li);
    }
}

function getOrderId(orderData) {
    return orderData.id;
}

function populateEditModal(orderData) {
    // Populate fields in the edit modal with orderData
    populateAllergiesList(orderData.allergies,orderData.allergies_options);
    populateDiateryList(orderData.dietary_restriction, orderData.dietary_restriction_options);
    document.getElementById('orderIdInput').value = getOrderId(orderData);
    document.getElementById('orderIdDisplay').textContent = getOrderId(orderData);


    // Populate other fields as needed
}

document.addEventListener("DOMContentLoaded", function() {
    // Get references to the form and buttons
    var saveBtn = document.getElementById('saveBtn');
    var deleteBtn = document.getElementById('deleteBtn');

    // Event listener for Save Changes button
    saveBtn.addEventListener('click', function() {
         // Retrieve order ID, allergies, and dietary restrictions
         var orderId = document.getElementById('orderIdInput').value;
         var allergies = getSelectedValues('allergiesList');
         var dietaryRestrictions = getSelectedValues('dietaryList');
         // Send data to Flask route via AJAX
         var data = {
             order_id: orderId,
             allergies: allergies,
             dietary_restrictions: dietaryRestrictions
         };	 
         fetch('/order_edit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (response.ok) {			
                window.location.href = "{{ url_for('views.index') }}";
            } else {
                // Request failed
                throw new Error('Request failed');
            }
        })
        .catch(error => {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
            // Redirect back to the index page
            window.location.href = "{{ url_for('views.index') }}";
        });
    });

    deleteBtn.addEventListener('click', function() {
        // Retrieve the order ID from the hidden input field or any other source
        var orderId = document.getElementById('orderIdInput').value;
        // Make an AJAX request to delete the order
        fetch('/order_delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ order_id: orderId })
        })
        .then(response => {
            if (response.ok) {
                // Request was successful
                // Reload the page after deletion
                window.location.reload();
            } else {
                // Request failed
                throw new Error('Failed to delete order');
            }
        })
        .catch(error => {
            // Handle any errors that occurred during the request
            console.error('Error:', error);
            // Display error message to the user or retry the request
        });
    });

    // Function to retrieve selected values from a list
    function getSelectedValues(listId) {
        var selectedValues = [];
        var checkboxes = document.querySelectorAll('#' + listId + ' input[type="checkbox"]');
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                selectedValues.push(checkbox.value);
            }
        });
        return selectedValues;
    }
    });