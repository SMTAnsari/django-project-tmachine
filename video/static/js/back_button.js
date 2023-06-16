// back_button.js
window.addEventListener('popstate', function (event) {
    window.location.href = '/'; // Redirect to the homepage
});

history.pushState(null, null, location.href);
window.onpopstate = function () {
    history.go(1);
};
