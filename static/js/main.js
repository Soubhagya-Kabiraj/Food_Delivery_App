// CraveX Main JavaScript File

document.addEventListener('DOMContentLoaded', function () {
    // Quantity Selector logic
    const qtyDecrements = document.querySelectorAll('.qty-btn-minus');
    const qtyIncrements = document.querySelectorAll('.qty-btn-plus');

    qtyDecrements.forEach(btn => {
        btn.addEventListener('click', function () {
            const input = this.nextElementSibling;
            if (input && input.tagName === 'INPUT') {
                let currentVal = parseInt(input.value) || 1;
                if (currentVal > 1) {
                    input.value = currentVal - 1;
                }
            }
        });
    });

    qtyIncrements.forEach(btn => {
        btn.addEventListener('click', function () {
            const input = this.previousElementSibling;
            if (input && input.tagName === 'INPUT') {
                let currentVal = parseInt(input.value) || 1;
                input.value = currentVal + 1;
            }
        });
    });

    // Auto-dismiss alerts after 4 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 4000);
    });
});
