// Assuming your flash message is inside an element with ID 'flash-message'
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.getElementById('flash-msg').style.display = 'none';
    }, 5000); // Hide the message after 5 seconds (adjust the time as needed)
});