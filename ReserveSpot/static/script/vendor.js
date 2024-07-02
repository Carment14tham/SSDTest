function showPage(page) {
    // Hide all tab pages
    var pages = document.querySelectorAll('.tab-page');
    pages.forEach(function (page) {
        page.classList.remove('active');
    });

    // Deactivate all tab buttons
    var buttons = document.querySelectorAll('.tab-button');
    buttons.forEach(function (button) {
        button.classList.remove('active');
    });

    // Show the selected page
    document.getElementById(page).classList.add('active');

    // Activate the corresponding button
    document.querySelector('.tab-button[onclick="showPage(\'' + page + '\')"]').classList.add('active');
}