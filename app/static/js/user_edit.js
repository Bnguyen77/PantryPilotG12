document.addEventListener('DOMContentLoaded', function() {
    const editBioForm = document.getElementById('editBioForm');
    const bioInput = document.getElementById('bioInput');
    const bioInputError = document.getElementById('bioInputError');

    editBioForm.addEventListener('submit', function(event) {
        if (!bioInput.value.trim()) {
            bioInput.classList.add('is-invalid');
            bioInputError.style.display = 'block';
            event.preventDefault(); // Prevent form submission if input is empty
        } else {
            bioInput.classList.remove('is-invalid');
            bioInputError.style.display = 'none';
        }
    });
});
