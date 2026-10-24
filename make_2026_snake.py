import os, subprocess, re
from datetime import datetime

raw = None
if os.path.exists('dist/github-contribution-grid-snake-dark.svg'):
    with open('dist/github-contribution-grid-snake-dark.svg', 'r', encoding='utf-8') as f:
        raw = f.read()
else:
    try:
        raw = subprocess.check_output(['git', 'show', 'origin/output:github-contribution-grid-snake-dark.svg']).decode('utf-8')
    except Exception:
        if os.path.exists('github-contribution-grid-snake-2026.svg'):
            with open('github-contribution-grid-snake-2026.svg', 'r', encoding='utf-8') as f:
                raw = f.read()

if not raw:
    print("No base SVG found to transform.")
    exit(0)

# Determine months up to current month (e.g. Oct)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
curr_month_idx = datetime.now().month - 1  # 0-indexed

month_texts = []
base_x = 230
spacing = 64

for i in range(min(curr_month_idx + 1, 10)):  # Display up to current month
    x = base_x + i * spacing
    name = months[i]
    if i == curr_month_idx:
        month_texts.append(f'  <text x="{x}" y="-12" font-weight="bold" fill="#39d353">{name} (Active) ⚡</text>')
    else:
        month_texts.append(f'  <text x="{x}" y="-12">{name}</text>')

labels = '<g fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11px">\n' + '\n'.join(month_texts) + '\n</g>'

new_svg = re.sub(r'viewBox="[^"]+"', 'viewBox="210 -36 670 176"', raw)
new_svg = re.sub(r'<g fill="#8b949e" font-family="-apple-system.*?<\/g>\s*<\/svg>', '</svg>', new_svg, flags=re.DOTALL)
new_svg = new_svg.replace('</svg>', f'{labels}\n</svg>')

with open('github-contribution-grid-snake-2026.svg', 'w', encoding='utf-8') as f:
    f.write(new_svg)

print("Updated github-contribution-grid-snake-2026.svg successfully!")

