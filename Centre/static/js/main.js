window.onload = function() {
    // Obtén los elementos del DOM
    var userMenuButton = document.getElementById('user-menu-button');
    var userMenu = document.getElementById('user-menu');
    var mobileMenuButton = document.getElementById('mobile-menu-button');
    var mobileMenu = document.getElementById('mobile-menu');

    // Asegúrate de que los elementos existen antes de agregar los event listeners
    if (userMenuButton && userMenu) {
        // Cuando se haga clic en el botón del menú del usuario, muestra u oculta el menú
        userMenuButton.addEventListener('click', function() {
            var isExpanded = userMenuButton.getAttribute('aria-expanded') === 'true';
            userMenuButton.setAttribute('aria-expanded', !isExpanded);
            userMenu.style.display = isExpanded ? 'none' : 'block';
        });
    }

    if (mobileMenuButton && mobileMenu) {
        // Cuando se haga clic en el botón del menú móvil, muestra u oculta el menú
        mobileMenuButton.addEventListener('click', function() {
            var isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
            mobileMenuButton.setAttribute('aria-expanded', !isExpanded);
            mobileMenu.style.display = isExpanded ? 'none' : 'block';
        });
    }
};