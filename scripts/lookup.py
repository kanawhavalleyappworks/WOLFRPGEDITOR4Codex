#!/usr/bin/env python3
"""Search the bundled WOLF references offline; Python standard library only."""
import argparse
from pathlib import Path
import re


def search(query, limit=12, root=None):
    folder = root or Path(__file__).resolve().parent.parent / 'references'
    tokens = re.findall(r'\S+', query.casefold())
    if not tokens:
        return []
    hits = []
    for path in sorted(folder.glob('*.md')):
        lines = path.read_text(encoding='utf-8').splitlines()
        for number, line in enumerate(lines, 1):
            if not line.strip() or line.startswith('| ---'):
                continue
            folded = line.casefold()
            if all(token in folded for token in tokens):
                score = sum(folded.count(token) for token in tokens) + (10 if query.casefold() in folded else 0)
                hits.append((score, path.name, number, line.strip()))
    hits.sort(key=lambda item: (-item[0], item[1], item[2]))
    return hits[:limit]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', help='All space-separated terms must appear within the same paragraph or table row')
    parser.add_argument('--limit', type=int, default=12)
    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error('--limit must be between 1 and 100')
    hits = search(args.query, args.limit)
    if not hits:
        print('No local matches. Try a command name, system ID, or fewer terms.')
        return 1
    for _, name, number, line in hits:
        # ASCII escapes keep output usable on legacy Windows console encodings.
        safe = line[:360].encode('ascii', errors='backslashreplace').decode('ascii')
        print(f'references/{name}:{number}: {safe}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
