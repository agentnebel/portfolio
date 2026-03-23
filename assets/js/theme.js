document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const root = document.documentElement;

    // We already checked and set the theme in the head to prevent flash.
    // This is just to ensure the logic works.
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        root.setAttribute('data-theme', savedTheme);
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            // Determine current theme
            let currentTheme = root.getAttribute('data-theme');
            
            // If not explicitly set via data-theme, derive from OS preference
            if (!currentTheme) {
                const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                currentTheme = prefersDark ? 'dark' : 'light';
            }

            // Toggle
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            // Apply and save
            root.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        });
    }
});
