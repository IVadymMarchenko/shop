
// Функция которая уменьшает навиг панель при прокрутке вниз
window.addEventListener('scroll', function(){
    document.getElementById('header-nav').classList.toggle('headernav-scroll',window.scrollY>135);
})


// Функция для вызова карусели
$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      
        responsiveClass:true,
        center:false,
        loop:true,
        nav:true,
        navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
        dots: true,
        autoplay: false,

        margin:10,
        responsive:{
            0:{
                items:1
            },
            500:{
                items:2
            },
            700:{
                items:2
            },
            1000:{
                items:4
            }
        }
    });
  });


// Получаем элементы
const button = document.getElementById('top');
const modal = document.getElementById('modal');
const closeBtn = document.querySelector('.close');

// Открытие модального окна при клике на кнопку
button.addEventListener('click', function() {
  modal.style.display = 'flex'; // Показать модальное окно
});

// Закрытие модального окна при клике на "крестик"
closeBtn.addEventListener('click', function() {
  modal.style.display = 'none'; // Скрыть модальное окно
});

// Закрытие модального окна при клике за пределы модального окна
window.addEventListener('click', function(event) {
  if (event.target === modal) {
    modal.style.display = 'none'; // Скрыть модальное окно
  }
});


// поворот стрелочки в фильтрах
document.querySelectorAll('.collapse-toggle').forEach(function(toggle) {
  toggle.addEventListener('click', function() {
    toggle.classList.toggle('collapsed');
  });
});







// Валидация формы
function updateStars(value) {
  stars.forEach(star => {
    if (star.getAttribute('data-value') <= value) {
      star.classList.add('active');
    } else {
      star.classList.remove('active');
    }
  });
}

// Валидация формы
function validateForm() {
  const name = document.getElementById('name').value;
  const review = document.getElementById('review').value;
  const rating = document.getElementById('rating').value;

  if (name === "" || review === "" || rating === "") {
    alert("Пожалуйста, заполните все поля и выберите оценку.");
    return false;
  }

  alert("Спасибо за ваш отзыв!");
  return true; // Здесь можно добавить отправку данных на сервер
}




// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()