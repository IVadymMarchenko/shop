$(document).ready(function() {
    $('.cart-qty').on('change', function(event) {
        event.preventDefault(); // Предотвращаем перезагрузку страницы

        let $input = $(this);
        let url = $input.data('url');
        let quantity = $input.val();

        if (quantity < 1) {
            quantity = 1;
            $input.val(1);
        }

        $.ajax({
            url: url,
            method: 'POST',
            data: {
                'quantity': quantity,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                if (response.message) {
                    // Обновляем значение инпута
                    $input.val(response.quantity);

                    // Логика для обновления общей суммы (предполагается, что у нас есть элемент с классом `.total-price`)
                    let totalPrice = 0;
                    $('.cart-qty').each(function() {
                        const price = parseFloat($(this).closest('tr').find('.product-price').text());
                        const qty = parseInt($(this).val(), 10);
                        totalPrice += price * qty;
                    });
                    $('.total-price').text(totalPrice.toFixed(2));
                }
            },
            error: function(xhr) {
                if (xhr.status === 403) {
                    alert("Please log in to update the cart.");
                } else {
                    console.error("An error occurred:", xhr.responseText);
                }
            }
        });
    });
});