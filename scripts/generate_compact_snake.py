"""Draw a compact snake using one pellet per actual GitHub contribution."""
import argparse
import json
import math
from pathlib import Path


def render(total, dark=False):
    count = min(total, 420)
    columns = min(35, max(1, math.ceil(count / 3)))
    rows = max(1, math.ceil(count / columns))
    pitch, margin = 24, 22
    width, height = columns * pitch + margin * 2, rows * pitch + margin * 2 + 22
    background = "#0d1117" if dark else "#ffffff"
    green = "#26a641" if dark else "#40c463"
    snake = "#c4b5fd" if dark else "#7c3aed"
    text = "#8b949e" if dark else "#57606a"
    points = []
    for row in range(rows):
        order = range(columns) if row % 2 == 0 else range(columns - 1, -1, -1)
        for column in order:
            if len(points) < count:
                points.append((margin + column * pitch + 12, margin + row * pitch + 12))
    title = f"{total:,} GitHub contributions in the past year"
    label = title if count == total else f"{count:,} squares shown · {title}"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">',
        f'<title id="title">{title}</title>',
        '<desc id="description">A compact animation with one square per contribution. Empty calendar days are omitted; positions do not represent dates.</desc>',
        f'<rect width="{width}" height="{height}" rx="12" fill="{background}"/>',
    ]
    duration = max(10, min(24, count * 0.13))
    for index, (x, y) in enumerate(points):
        eaten = 0.02 + 0.82 * index / max(1, count - 1)
        parts.append(
            f'<rect x="{x - 7}" y="{y - 7}" width="14" height="14" rx="3" fill="{green}">'
            f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;{eaten:.5f};{eaten + 0.008:.5f};0.96;1" dur="{duration}s" repeatCount="indefinite"/>'
            '</rect>'
        )
    if points:
        path = "M " + " L ".join(f"{x},{y}" for x, y in points)
        if len(points) == 1:
            path += f" L {points[0][0] + 0.01},{points[0][1]}"
        for segment in range(5, -1, -1):
            delay = segment * duration * 0.82 / max(1, count - 1)
            radius = 6.5 if segment == 0 else 5.8
            parts.append(
                f'<g><circle r="{radius}" fill="{snake}"/>'
                + ('<circle cx="2" cy="-2" r="1.3" fill="#ffffff"/>' if segment == 0 else '')
                + f'<animateMotion path="{path}" dur="{duration}s" begin="{delay:.4f}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;0.85;1" calcMode="linear"/></g>'
            )
    else:
        label = "No contributions in this period"
    parts.append(f'<text x="{margin}" y="{height - 12}" fill="{text}" font-family="system-ui, sans-serif" font-size="11">{label}</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    count = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    if not isinstance(count, int) or count < 0:
        raise ValueError("Expected a nonnegative contribution count from GitHub")
    args.output.mkdir(parents=True, exist_ok=True)
    for dark, name in [(False, "compact-snake.svg"), (True, "compact-snake-dark.svg")]:
        (args.output / name).write_text(render(count, dark), encoding="utf-8")


if __name__ == "__main__":
    main()
