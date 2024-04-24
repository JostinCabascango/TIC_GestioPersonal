window.addEventListener('load', () => {
    const toggleMenuVisibility = (buttonId, menuSelector) => {
        const button = document.getElementById(buttonId);
        const menu = document.querySelector(menuSelector);

        if (button && menu) {
            button.addEventListener('click', () => {
                menu.classList.toggle('hidden');
            });
        }
    };

    toggleMenuVisibility('user-menu-button', '[aria-labelledby="user-menu-button"]');
    toggleMenuVisibility('mobile-menu-button', '#mobile-menu');
});