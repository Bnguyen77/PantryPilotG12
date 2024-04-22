// SCRIPT for CREATING NEW ORDERS


// FOR ORDER REQUEST FORM
const enableItemsCheckbox = document.getElementById('enableItems');
const enableRestrictionsCheckbox = document.getElementById('enableRestrictions');
const enableLocationCheckbox = document.getElementById('enableLocation');
const itemsInput = document.getElementById('items');
const restrictionInput = document.getElementById('restriction');
const locationInput = document.getElementById('location');
const deliverButton = document.getElementById('deliver');
const deliveryAddress = document.getElementById('delivery-address');

function updateInputValue(
	checkbox,
	inputField,
	defaultValue
) {
	if (checkbox.checked) {
		if (inputField.value.trim() === '') {
			inputField.value = defaultValue;
			// Set the default value if the input field is empty -->
		}
	} else {
		inputField.value = ''; // Clear the value if the checkbox is unchecked
	}
	inputField.disabled = !checkbox.checked;
}

// Add event listener to the enableItemsCheckbox
enableItemsCheckbox.addEventListener('change', function () {
	itemsInput.disabled = !enableItemsCheckbox.checked;
	updateInputValue(enableItemsCheckbox, itemsInput, 'None');
	itemsInput.placeholder = enableItemsCheckbox.checked
		? 'Enter Prefer Items'
		: 'No Item Reference';
});

// Add event listener to the enableRestrictionsCheckbox
enableRestrictionsCheckbox.addEventListener('change', function () {
	restrictionInput.disabled = !enableRestrictionsCheckbox.checked;
	restrictionInput.placeholder = enableRestrictionsCheckbox.checked
		? 'Enter Dietary Restrictions'
		: 'No Dietary Restriction';
	updateInputValue(enableRestrictionsCheckbox, restrictionInput, 'None');
});

// Add event listener to the enableLocationCheckbox
enableLocationCheckbox.addEventListener('change', function () {
	locationInput.disabled = !enableLocationCheckbox.checked;
	locationInput.placeholder = enableLocationCheckbox.checked
		? 'Enter Delivery Address'
		: 'UIC Student Center';
	updateInputValue(enableLocationCheckbox, locationInput, 'UIC');
});

//END ORDER REQUEST FORM




