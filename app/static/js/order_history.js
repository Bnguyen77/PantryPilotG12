//DISPLAYING ORDER HISTORY SORTING BUTTONs

document.addEventListener('DOMContentLoaded', function () {
	// Get references to the buttons and order list
	const deliveryBtn = document.getElementById('deliveryBtn');
	const pickupBtn = document.getElementById('pickupBtn');
	const completeBtn = document.getElementById('completeBtn');
	const confirmBtn = document.getElementById('confirmBtn');
	const orderList = document.getElementById('orderList');

	// Function to reset the display of all orders
	function resetOrderDisplay() {
		const orders = orderList.querySelectorAll('.list-group-item');
		orders.forEach((order) => {
			order.style.display = 'block';
		});
	}
	// Add event listener to the complete button
	completeBtn.addEventListener('click', function () {
		// Show only orders with status "complete"
		const orders = orderList.querySelectorAll('.list-group-item');
		orders.forEach((order) => {
			if (order.dataset.status === 'completed') {
				order.style.display = 'block';
			} else {
				order.style.display = 'none';
			}
		});
	});

	confirmBtn.addEventListener('click', function () {
		// Show only orders with status "complete"
		const orders = orderList.querySelectorAll('.list-group-item');
		orders.forEach((order) => {
			if (order.dataset.status === 'confirmed') {
				order.style.display = 'block';
			} else {
				order.style.display = 'none';
			}
		});
	});

	// Add event listener to the pending button (optional)
	deliveryBtn.addEventListener('click', function () {
		// Show all orders
		const orders = orderList.querySelectorAll('.list-group-item');
		orders.forEach((order) => {
			if (order.dataset.delivery === 'True' && order.dataset.status === 'pending') {
				order.style.display = 'block';
			} else {
				order.style.display = 'none';
			}
		});
	});

	pickupBtn.addEventListener('click', function () {
		// Show all orders
		const orders = orderList.querySelectorAll('.list-group-item');
		orders.forEach((order) => {
			if (order.dataset.delivery === 'False' && order.dataset.status === 'pending') {
				order.style.display = 'block';
			} else {
				order.style.display = 'none';
			}
		});
	});


	//reseting display when modal is closed
	$('#orderHistoryModal').on('shown.bs.modal', function () {
		// Reset the display of all orders
		resetOrderDisplay();
	});
});

//END - DISPLAY ORDERS HISTORY
