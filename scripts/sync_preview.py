"""Refresh the self-contained Still preview; Python standard library only."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
css = (root / "themes/still/still.css").read_text()
page = root / "themes/still/preview.html"
html = page.read_text()
opening = '<style id="theme-preview">'
start = html.index(opening) + len(opening)
end = html.index('</style>', start)
page.write_text(html[:start] + css + html[end:])
print(f"Preview updated ({len(css.encode())} CSS bytes).")
