document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector("header");

    // Отримання висоти верхнього колонтитулу
    const headerHeight = header.offsetHeight;

    // Функція для перевірки прокрутки та застосування класу
    function checkScroll() {
        if (window.scrollY > headerHeight) {
            header.classList.add("fixed");
        } else {
            header.classList.remove("fixed");
        }
    }

    // Викликати функцію при прокрутці сторінки
    window.addEventListener("scroll", checkScroll);

    // Викликати функцію відразу для перевірки при завантаженні сторінки
    checkScroll();
});