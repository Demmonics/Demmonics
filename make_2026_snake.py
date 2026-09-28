import os, subprocess, re

if os.path.exists('dist/github-contribution-grid-snake-dark.svg'):
    with open('dist/github-contribution-grid-snake-dark.svg', 'r', encoding='utf-8') as f:
        raw = f.read()
else:
    raw = subprocess.check_output(['git', 'show', 'origin/output:github-contribution-grid-snake-dark.svg']).decode('utf-8')

labels = '''
<g fill="#8b949e" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" font-size="11px">
  <text x="230" y="-12">Jan</text>
  <text x="294" y="-12">Feb</text>
  <text x="358" y="-12">Mar</text>
  <text x="422" y="-12">Apr</text>
  <text x="486" y="-12">May</text>
  <text x="550" y="-12">Jun</text>
  <text x="614" y="-12">Jul</text>
  <text x="678" y="-12">Aug</text>
  <text x="742" y="-12" font-weight="bold" fill="#39d353">Sep (Active) ⚡</text>
</g>
'''

new_svg = re.sub(r'viewBox="[^"]+"', 'viewBox="210 -36 650 176"', raw)
new_svg = new_svg.replace('</svg>', f'{labels}</svg>')

with open('github-contribution-grid-snake-2026.svg', 'w', encoding='utf-8') as f:
    f.write(new_svg)

print("Updated github-contribution-grid-snake-2026.svg successfully!")
