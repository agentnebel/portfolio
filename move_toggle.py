import os
import re

base_dir = '/data/.openclaw/workspace/portfolio/'
html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# The block we want to move
toggle_regex = re.compile(r'\s*<div class="mood-toggle-wrapper">.*?</div>\s*', re.DOTALL)

for file in html_files:
    path = os.path.join(base_dir, file)
    with open(path, 'r') as f:
        content = f.read()

    # Extract the toggle block
    match = toggle_regex.search(content)
    if not match:
        continue
    toggle_block = match.group(0)

    # Remove the toggle block from its original position
    content = content.replace(toggle_block, '\n            ')

    # Clean up the toggle block formatting for insertion
    clean_toggle = toggle_block.strip()
    # Add indentation
    indented_toggle = '\n                ' + clean_toggle.replace('\n', '\n                ') + '\n            '

    # Find the end of main-nav
    nav_end_idx = content.find('</nav>')
    if nav_end_idx != -1:
        # Insert the toggle block right before </nav>
        content = content[:nav_end_idx] + indented_toggle + content[nav_end_idx:]

    with open(path, 'w') as f:
        f.write(content)

# Update CSS
css_path = os.path.join(base_dir, 'assets/css/style.css')
with open(css_path, 'r') as f:
    css = f.read()

old_css_1 = """/* MOOD TOGGLE */
.mood-toggle-wrapper {
    position: absolute;
    right: 20px;
    top: 25px;
    display: flex;
    align-items: center;
    gap: 12px;
    z-index: 100;
}"""
new_css_1 = """/* MOOD TOGGLE */
.mood-toggle-wrapper {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-left: 20px;
}"""

old_css_2 = """    /* Adjust right side (toggle) */
    .mood-toggle-wrapper {
        position: relative;
        right: auto;
        top: auto;
        margin-top: 0;
        z-index: 1002;
    }
    
    .mood-label {
        display: none;
    }"""
new_css_2 = """    /* Adjust right side (toggle) */
    .mood-toggle-wrapper {
        margin-top: 20px;
        margin-left: 0;
    }
    
    .mood-label {
        display: block;
        color: var(--text-color);
        font-size: 18px;
    }"""

css = css.replace(old_css_1, new_css_1)
css = css.replace(old_css_2, new_css_2)

# Also ensure `.main-nav` has `align-items: center;` for desktop so the toggle aligns vertically with text
if ".main-nav {\n    display: flex;\n    gap: 40px;\n    flex-wrap: wrap;\n    justify-content: center;\n}" in css:
    css = css.replace(
        ".main-nav {\n    display: flex;\n    gap: 40px;\n    flex-wrap: wrap;\n    justify-content: center;\n}",
        ".main-nav {\n    display: flex;\n    gap: 40px;\n    flex-wrap: wrap;\n    justify-content: center;\n    align-items: center;\n}"
    )

with open(css_path, 'w') as f:
    f.write(css)

print("Done updating HTML and CSS!")
