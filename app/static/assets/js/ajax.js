$(document).on('click', '.add-to-cart', function(event) {
    event.preventDefault();

    const productId = $(this).data('product-id');
    const csrftoken = $('meta[name="csrf-token"]').attr('content');
    

    if (!csrftoken) return console.error("CSRF-токен не найден.");

    $.ajax({
        url: '/cart/cart_add/',
        type: 'POST',
        data: { product_id: productId },
        headers: { 'X-CSRFToken': csrftoken },
        dataType: 'json',
        success: function({ message, cart_items_html, cart_offcanvas_html, total_items }) {
            const notification = $('#jq-notification');
            notification.text(message)
                .stop(true, true) // Останавливаем любые текущие анимации
                .fadeIn(30) // Плавное появление
                .delay(1000) // Задержка перед исчезновением
                .fadeOut(300); // Плавное исчезновение

            $('#cart-items-container').html(cart_items_html);
            $('#offcanvasCart .offcanvas-body').html(cart_offcanvas_html);
            $('.card-badge').text(total_items);
        },
        error: function() {
            console.error("Ошибка при добавлении товара.");
        }
    });
});








