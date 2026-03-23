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

// --- CUSTOM CURSOR FOR IMAGES ---
document.addEventListener('DOMContentLoaded', () => {
    // Inject custom cursor
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

    // Detect hover on gallery images
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

// --- DYNAMIC GRID FORMAT (Portrait/Landscape) ---
document.addEventListener('DOMContentLoaded', () => {
    const gridItems = document.querySelectorAll('.grid-item');
    
    gridItems.forEach(item => {
        const img = item.querySelector('img');
        if (!img) return;

        const applyFormat = () => {
            const ratio = img.naturalWidth / img.naturalHeight;
            // Add classes based on the actual image aspect ratio
            if (ratio > 1.1) {
                item.classList.add('landscape');
            } else {
                item.classList.add('portrait');
            }
        };

        if (img.complete) {
            applyFormat();
        } else {
            img.addEventListener('load', applyFormat);
        }
    });
});
