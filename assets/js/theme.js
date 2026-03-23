document.addEventListener('DOMContentLoaded', () => {
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
});
