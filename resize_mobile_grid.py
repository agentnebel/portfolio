import sys

css_path = '/data/.openclaw/workspace/portfolio/assets/css/style.css'
with open(css_path, 'r') as f:
    content = f.read()

old_mobile_grid = """@media (max-width: 768px) {
    .masonry-gallery {
        column-count: 1;
        column-gap: 0;
    }
    .grid-item {
        margin-bottom: 20px;
    }
}"""

new_mobile_grid = """@media (max-width: 768px) {
    .masonry-gallery {
        column-count: 2;
        column-gap: 3vw;
    }
    .grid-item {
        margin-bottom: 3vw;
    }
}"""

content = content.replace(old_mobile_grid, new_mobile_grid)

with open(css_path, 'w') as f:
    f.write(content)
