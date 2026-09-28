import urllib.request
import re
from datetime import datetime, date

def generate_svg():
    url = 'https://github.com/users/Demmonics/contributions?from=2026-01-01&to=2026-12-31'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')

    total_match = re.search(r'([0-9,]+)\s+contributions\s+in\s+2026', html, re.IGNORECASE)
    total_contribs = total_match.group(1) if total_match else "421"

    # Map dates to level
    matches = re.findall(r'<td[^>]*data-date="(\d{4}-\d{2}-\d{2})"[^>]*data-level="(\d+)"[^>]*>', html)
    date_to_level = {m[0]: int(m[1]) for m in matches}

    # Color palette for dark mode (classic GitHub Dark Dimmed / High Contrast)
    colors = {
        0: "#161b22",
        1: "#0e4429",
        2: "#006d32",
        3: "#26a641",
        4: "#39d353"
    }

    # Layout constants
    cell_size = 11
    cell_gap = 3
    col_width = cell_size + cell_gap
    start_x = 45
    start_y = 52
    
    # 2026 starts on Thursday (day 4, where Sunday is 0)
    # Let's map each day of 2026 to (col, row)
    start_date = date(2026, 1, 1)
    end_date = date(2026, 12, 31)

    # In GitHub, row 0 is Sunday, row 6 is Saturday
    # Python weekday(): Monday is 0, Sunday is 6 -> convert to Sun=0: (dt.weekday() + 1) % 7
    rects = []
    month_labels = {}
    
    # Track current col
    cur_date = start_date
    first_sun_offset = (cur_date.weekday() + 1) % 7
    col = 0

    from datetime import timedelta
    cur = start_date
    while cur <= end_date:
        dow = (cur.weekday() + 1) % 7
        if dow == 0 and cur != start_date:
            col += 1
        
        # Check month label
        if cur.day == 1:
            month_name = cur.strftime("%b")
            month_labels[col] = month_name
            
        d_str = cur.strftime("%Y-%m-%d")
        lvl = date_to_level.get(d_str, 0)
        c = colors.get(lvl, colors[0])
        
        x = start_x + col * col_width
        y = start_y + dow * col_width
        
        anim_delay = (col * 15 + dow * 5)
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{c}" '
            f'class="cell" data-date="{d_str}" data-level="{lvl}" '
            f'style="animation-delay: {anim_delay}ms;">'
            f'<title>{d_str}: {lvl} level</title></rect>'
        )
        cur += timedelta(days=1)

    total_cols = col + 1
    svg_width = start_x + total_cols * col_width + 30
    svg_height = 195

    # Month text labels
    months_svg = []
    for c_idx, m_name in month_labels.items():
        mx = start_x + c_idx * col_width
        months_svg.append(f'<text x="{mx}" y="40" class="month-label">{m_name}</text>')

    # Day labels (Mon, Wed, Fri)
    days_svg = [
        f'<text x="18" y="{start_y + 1 * col_width + 9}" class="day-label">Mon</text>',
        f'<text x="18" y="{start_y + 3 * col_width + 9}" class="day-label">Wed</text>',
        f'<text x="18" y="{start_y + 5 * col_width + 9}" class="day-label">Fri</text>',
    ]

    # Legend
    legend_x = svg_width - 160
    legend_y = svg_height - 24
    legend_items = [
        f'<text x="{legend_x - 32}" y="{legend_y + 9}" class="legend-label">Less</text>'
    ]
    for i in range(5):
        lx = legend_x + i * (cell_size + 3)
        legend_items.append(f'<rect x="{lx}" y="{legend_y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{colors[i]}" />')
    legend_items.append(f'<text x="{legend_x + 5 * (cell_size + 3) + 4}" y="{legend_y + 9}" class="legend-label">More</text>')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}">
  <style>
    .bg {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }}
    .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 15px; font-weight: 600; fill: #f0f6fc; }}
    .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #8b949e; }}
    .month-label {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; fill: #8b949e; }}
    .day-label {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; fill: #8b949e; }}
    .legend-label {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; fill: #8b949e; }}
    @keyframes pulseFade {{
      0% {{ opacity: 0.1; transform: scale(0.9); }}
      100% {{ opacity: 1; transform: scale(1); }}
    }}
    .cell {{
      transform-origin: center;
      animation: pulseFade 0.4s ease-out both;
    }}
    .cell:hover {{
      stroke: #ffffff;
      stroke-width: 1px;
    }}
  </style>

  <rect width="100%" height="100%" class="bg" />

  <!-- Title & Total -->
  <text x="24" y="24" class="title">2026 Contribution Activity</text>
  <text x="{svg_width - 24}" y="24" text-anchor="end" class="subtitle">{total_contribs} contributions in 2026</text>

  <!-- Month Labels -->
  {''.join(months_svg)}

  <!-- Day Labels -->
  {''.join(days_svg)}

  <!-- Contribution Grid -->
  {''.join(rects)}

  <!-- Legend -->
  {''.join(legend_items)}
</svg>'''

    with open('contribution-heatmap-2026.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Successfully generated contribution-heatmap-2026.svg")

if __name__ == '__main__':
    generate_svg()
