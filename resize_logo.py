import sys

css_path = '/data/.openclaw/workspace/portfolio/assets/css/style.css'
with open(css_path, 'r') as f:
    content = f.read()

old_desktop_logo = """.logo {
    font-size: 36px;"""
new_desktop_logo = """.logo {
    font-size: 48px;"""

old_mobile_logo = """    .logo {
        font-size: 24px;"""
new_mobile_logo = """    .logo {
        font-size: 32px;"""

content = content.replace(old_desktop_logo, new_desktop_logo)
content = content.replace(old_mobile_logo, new_mobile_logo)

with open(css_path, 'w') as f:
    f.write(content)
