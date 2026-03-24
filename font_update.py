import sys

css_path = '/data/.openclaw/workspace/portfolio/assets/css/style.css'
with open(css_path, 'r') as f:
    content = f.read()

# Replace variables
old_vars = """    /* Typography */
    --font-primary: 'Rubik', sans-serif;
}"""
new_vars = """    /* Typography */
    --font-primary: 'Space Mono', monospace;
    --font-display: 'Syne', sans-serif;
}"""
content = content.replace(old_vars, new_vars)

# Logo / Display font
old_logo = """.logo {
    font-size: 48px;
    font-weight: 900;"""
new_logo = """.logo {
    font-family: var(--font-display);
    font-size: 48px;
    font-weight: 800;"""
content = content.replace(old_logo, new_logo)

old_nav = """.main-nav a {
    font-size: 18px;
    letter-spacing: -0.5px;
    color: var(--nav-color);
    text-transform: uppercase;
    font-weight: 800;"""
new_nav = """.main-nav a {
    font-size: 16px;
    letter-spacing: 1px;
    color: var(--nav-color);
    text-transform: uppercase;
    font-weight: 700;"""
content = content.replace(old_nav, new_nav)

old_mobile_nav = """.main-nav a {
        font-size: 28px;
        
        
        color: var(--text-color);
    }"""
new_mobile_nav = """.main-nav a {
        font-size: 24px;
        letter-spacing: 2px;
        color: var(--text-color);
    }"""
content = content.replace(old_mobile_nav, new_mobile_nav)

old_mood = """.mood-label {
    font-size: 14px;
    letter-spacing: -0.2px;
    text-transform: uppercase;
    font-weight: 800;"""
new_mood = """.mood-label {
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: 700;"""
content = content.replace(old_mood, new_mood)

with open(css_path, 'w') as f:
    f.write(content)

# Update HTML files to import the new fonts
import glob

html_files = glob.glob('/data/.openclaw/workspace/portfolio/*.html')
old_font_import = '<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">'
new_font_import = '<link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Syne:wght@400..800&display=swap" rel="stylesheet">'

for file in html_files:
    with open(file, 'r') as f:
        html = f.read()
    html = html.replace(old_font_import, new_font_import)
    with open(file, 'w') as f:
        f.write(html)

print("Fonts updated!")
