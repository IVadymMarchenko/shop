$(document).on('click', '.add-to-cart', function(event) {
    event.preventDefault();

    const productId = $(this).data('product-id');
    const csrfTokenElement = document.querySelector('[name=csrf-token]');

    if (!csrfTokenElement) {
        console.error("CSRF-токен не найден.");
        return;
    }

    const csrftoken = csrfTokenElement.getAttribute('content');

    $.ajax({
        url: '/cart/cart_add/',
        type: 'POST',
        data: { product_id: productId },
        headers: { 'X-CSRFToken': csrftoken },
        success: function(data) {
            console.log("Успешный ответ:", data);
            $('#cart-items-container').html(data.cart_items_html);
            $('#offcanvasCart .offcanvas-body').html(data.cart_offcanvas_html);  // Убедитесь, что селектор правильный

            const badgeElement = document.querySelector('.card-badge');
            if (badgeElement) {
                badgeElement.textContent = data.total_items;
            }
        },
        error: function(xhr, status, error) {
            console.error("Ошибка:", error);
        }
    });
});
