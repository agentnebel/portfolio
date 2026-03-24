import sys
css_path = '/data/.openclaw/workspace/portfolio/assets/css/style.css'
with open(css_path, 'r') as f:
    css = f.read()

old_mobile_logo = """    .logo {
        font-size: 32px;
        z-index: 1002;"""
new_mobile_logo = """    .logo {
        font-size: 36px;
        letter-spacing: -2px;
        z-index: 1002;"""
css = css.replace(old_mobile_logo, new_mobile_logo)

with open(css_path, 'w') as f:
    f.write(css)
