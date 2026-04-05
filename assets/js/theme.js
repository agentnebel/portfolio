document.addEventListener('DOMContentLoaded', () => {
    // --- THEME TOGGLE ---
    const toggleCheckbox = document.getElementById('theme-toggle-checkbox');
    const root = document.documentElement;

    let currentTheme = localStorage.getItem('theme');
    if (!currentTheme) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        currentTheme = prefersDark ? 'dark' : 'light';
    }
    
    root.setAttribute('data-theme', currentTheme);
    
    if (toggleCheckbox) {
        toggleCheckbox.checked = currentTheme === 'dark';

        toggleCheckbox.addEventListener('change', (e) => {
            const newTheme = e.target.checked ? 'dark' : 'light';
            root.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }

    // --- MOBILE MENU ---
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');
    if(mobileBtn && mainNav) {
        const setMenuState = (isOpen) => {
            mobileBtn.classList.toggle('active', isOpen);
            mainNav.classList.toggle('active', isOpen);
            document.body.classList.toggle('menu-open', isOpen);
            mobileBtn.setAttribute('aria-expanded', String(isOpen));
        };

        mobileBtn.addEventListener('click', () => {
            const isOpen = !mainNav.classList.contains('active');
            setMenuState(isOpen);
        });

        mainNav.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => {
                setMenuState(false);
            });
        });

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') {
                setMenuState(false);
            }
        });
    }

    // --- CUSTOM CURSOR FOR IMAGES ---
    const cursor = document.createElement('div');
    cursor.classList.add('custom-cursor');
    document.body.appendChild(cursor);

    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        cursor.style.left = mouseX + 'px';
        cursor.style.top = mouseY + 'px';
    });

    const images = document.querySelectorAll('.grid-item img');
    images.forEach(img => {
        img.addEventListener('mouseenter', () => {
            document.body.classList.add('hovering-img');
        });
        img.addEventListener('mouseleave', () => {
            document.body.classList.remove('hovering-img');
        });
    });
});
