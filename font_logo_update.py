import sys
import glob

css_path = '/data/.openclaw/workspace/portfolio/assets/css/style.css'
with open(css_path, 'r') as f:
    css = f.read()

# Replace variables
old_vars = """    --font-display: 'Syne', sans-serif;"""
new_vars = """    --font-display: 'Archivo Black', sans-serif;"""
css = css.replace(old_vars, new_vars)

# Logo adjustments
old_logo = """.logo {
    font-family: var(--font-display);
    font-size: 48px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
    text-transform: uppercase;
}"""
new_logo = """.logo {
    font-family: var(--font-display);
    font-size: 52px;
    font-weight: 400;
    letter-spacing: -2.5px;
    line-height: 1.1;
    text-transform: uppercase;
}"""
css = css.replace(old_logo, new_logo)

with open(css_path, 'w') as f:
    f.write(css)

# Update HTML files
html_files = glob.glob('/data/.openclaw/workspace/portfolio/*.html')
old_font_import = '<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Syne:wght@400..800&display=swap" rel="stylesheet">'
new_font_import = '<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Archivo+Black&display=swap" rel="stylesheet">'

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
    html = html.replace(old_font_import, new_font_import)
    with open(file, 'w') as f:
        f.write(html)

print("Logo Font updated!")
